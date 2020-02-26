from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, StickerSendMessage, AudioSendMessage, QuickReply, QuickReplyButton, DatetimePickerAction
)
import datetime


import destination_parser
import member_parser
import time_parser


# Steps
# 0: dest
# 2: dest_receiver
# 3: time_receiver
# 4: member_receiver

class Session:
    def __init__(self, group_id):
        self.group_id = group_id
        self.step = 0
        self.destination = ""
        self.members = []
        self.arrive_time = None

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
        return TextSendMessage("目的地は{}だね．次は到着時間を入力してね．".format(self.destination))

    def time_receiver(self, event):
        self.step += 1
        self.arrive_time = time_parser.time_parser(event)
        return TextSendMessage("到着時間は{}だね．次はメンバーを入力してね．".format(self.arrive_time))

    def member_receiver(self, event):
        self.step += 1
        #self.members = event.message.text.split(",")
        self.members = member_parser.member_parser(event)
        return TextSendMessage("メンバーは{}だね．".format(self.members))
