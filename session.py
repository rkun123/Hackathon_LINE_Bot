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
import yandere


# Steps
# 0: dest
# 2: dest_receiver
# 3: time_receiver
# 4: member_receiver

class Session:
    def __init__(self, group_id, api):
        self.group_id = group_id
        self.api = api
        self.step = 0
        self.destination = ""
        self.members = []
        self.arrival_time = None

    # returns *SendMessage
    def execute(self, event):
        if self.step == 0:
            return self.dest(event)

        elif self.step == 1:
            return self.dest_receiver(event)

        elif self.step == 2:
            return self.time_receiver(event)

        elif self.step == 3:
            return self.member_receiver(event)
        
        else:
            self.step = 0
            return TextSendMessage("Finish")

    def dest(self, event):
        self.step += 1
        return TextSendMessage("目的地を入力してね")

    def dest_receiver(self, event):
        self.step += 1
        self.destination = destination_parser.destination_parser(event)
        return TextSendMessage(text="目的地は{}だね．次は到着時間を入力してね．".format(self.destination), quick_reply=QuickReply(items=[
            QuickReplyButton(
                action=DatetimePickerAction(
                    label="到着時間",
                    data="arrival_time",
                    mode="datetime"
                    )
                )
            ])
            )

    def time_receiver(self, event):
        self.step += 1
        self.arrival_time = time_parser.time_parser(event)
        print(self.arrival_time)
        return TextSendMessage("到着時間は{}だね．次はメンバーを入力してね．".format(self.arrival_time))

    def member_receiver(self, event):
        self.step += 1
        #self.members = event.message.text.split(",")
        self.members = member_parser.member_parser(event)
        self.reserve(self.arrival_time, event)
        return TextSendMessage("メンバーは{}だね．\n{}".format(self.members, progress_bar.progress_bar(3, 10)))


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
            if datetime.datetime.now() >= arrival_datetime:
                yandere.yandere_negative(api, event, ["aa"])
                break
            time.sleep(1)
