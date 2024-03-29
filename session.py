from linebot.exceptions import LineBotApiError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, StickerSendMessage, AudioSendMessage, QuickReply, QuickReplyButton, DatetimePickerAction
)
import datetime
import threading
import time


import destination_parser
import member_parser
import time_parser
import progress_bar
import template_message_generator
import yandere
import messages


class Session:
    def __init__(self, group_id, api):
        self.group_id = group_id
        self.api = api
        self.step = 0
        self.destination = ""
        self.members = set()
        self.arrived_members = set()
        self.arrival_time = None

    def display_name_by_id(self, id):
        try:
            profile = self.api.get_profile(id)
            return profile
        except LineBotApiError as e:
            return None

    # returns *SendMessage
    def execute(self, event):
        if event.type is "message" and event.message.type is "text" and "キャンセル" in event.message.text:
            self.step = 0
            return TextSendMessage(text="キャンセルしました")
        elif self.step == 0:
            return self.dest(event)

        elif self.step == 1:
            return self.dest_receiver(event)

        elif self.step == 2:
            return self.time_receiver(event)

        elif self.step == 3:
            return self.member_receiver(event)

        elif self.step == 4:
            return self.member_arrival_receiver(event)

        else:
            self.step = 0
            return TextSendMessage("Finish")

    def dest(self, event):
        if "ヤンデレ" in event.message.text:
            self.step += 1
            return template_message_generator.arrival_locationpicker()
            # return TextSendMessage(messages.messages("input_destination"))
        return None

    def dest_receiver(self, event):
        self.step += 1
        self.destination = destination_parser.destination_parser(event)
        return template_message_generator.arrival_datepicker(self.destination)

    def time_receiver(self, event):
        self.step += 1
        self.arrival_time = time_parser.time_parser(event)
        print(self.arrival_time)
        # return TextSendMessage(messages.messages("invited_person").format(self.arrival_time))
        return template_message_generator.member_text(self.arrival_time)

    def member_receiver(self, event):
        self.step += 1
        self.members = set(member_parser.member_parser(event))
        # Add source user
        self.members.add("@"+self.display_name_by_id(event.source.user_id).display_name)
        print(self.members)
        self.api.push_message(event.source.group_id, messages=TextSendMessage(text="参加者は{}だね．".format(self.members)))
        self.api.reply_message(event.reply_token, template_message_generator.arrival_button())
        self.reserve(self.arrival_time, event)

    def member_arrival_receiver(self, event):
        if event.type is not "postback":
            return None
        print("user_id: "+event.source.user_id)
        user_name = "@"+self.display_name_by_id(event.source.user_id).display_name
        print(user_name)

        if user_name not in self.members:
            # return TextSendMessage(messages.messages("unjoined_user_arrived").format(user_name[1:]))
            return None

        if user_name in self.arrived_members:
            # return TextSendMessage(messages.messages("duplicated_user_arrived").format(user_name[1:]))
            return None

        self.arrived_members.add(user_name)
        print(self.arrived_members)

        return TextSendMessage(progress_bar.progress_bar(len(self.arrived_members), len(self.members)))


    def reserve(self, arrival_datetime, event):
        pending = threading.Thread(name="arrival_timer", target=self.arrival_notify, args=(self.api, arrival_datetime, event))
        pending.start()
        print("ArrivalPending has started")
        pending.join()

    def arrival_notify(self, api, arrival_datetime, event):
        print("now: ")
        print(datetime.datetime.now())
        print("target: ")
        print(arrival_datetime)
        while True:
            print(".")
            if len(self.members) == len(self.arrived_members):
                self.step = 0
                break
            if datetime.datetime.now() >= arrival_datetime:
                self.api.push_message(self.group_id, template_message_generator.arrival_timer_breaked())
                yandere.yandere_negative(api, event, list(self.members - self.arrived_members))
                arrival_datetime += datetime.timedelta(minutes=1)
            time.sleep(1)
