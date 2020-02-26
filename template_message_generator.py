import re, datetime
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, LocationMessage, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction, PostbackAction, FlexSendMessage, BubbleContainer, BubbleStyle, BoxComponent, ButtonComponent, TextComponent, ImageComponent, BlockStyle, LocationAction
)

import os

def arrival_locationpicker(msg):
    return FlexSendMessage("目的地設定", BubbleContainer(
        size="micro",
        # hero=ImageComponent(url="https://via.placeholder.com/500"),
        body=BoxComponent(
            layout="vertical",
            contents=[ 
                TextComponent(
                    text=msg,
                    size="sm"
                ),
                ButtonComponent(
                    style="link",
                    height="sm",
                    action=LocationAction(
                        label="目的地設定"
                    )
                )]
        ),
        styles=BubbleStyle(body=BlockStyle(background_color="#ffffff"))
    ))


def arrival_datepicker(msg):
    now_date = datetime.datetime.now().isoformat()
    regex  = re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{2}:[0-9]{2}", now_date)
    tstr = regex[0] + "T" + regex[1]

    return FlexSendMessage("集合時間", BubbleContainer(
        size="mega",
        # hero=ImageComponent(url="https://via.placeholder.com/500"),
        body=BoxComponent(
            layout="vertical",
            contents=[
                TextComponent(
                    text=msg,
                    size="sm"
                ),
                ButtonComponent(
                    style="link",
                    height="sm",
                    action=DatetimePickerTemplateAction(
                        label="集合時間設定",
                        data="action=buy&itemid=2&mode=datetime",
                        mode="datetime",
                        initial=tstr,
                        min=tstr,
                        max="2099-12-31T23:59"
                    )
                )
            ]
        ),
        styles=BubbleStyle(body=BlockStyle(background_color="#ffffff"))
    ))

def arrival_button():
    return FlexSendMessage("到着", BubbleContainer(
        size="micro",
        body=BoxComponent(
            layout="vertical",
            contents=[
                ButtonComponent(
                    style="link",
                    height="sm",
                    action=PostbackAction(
                        label="到着",
                        display_text="到着",
                        data="data not served"
                    )
                )
            ]
        ),
        action=PostbackAction(
            label="到着",
            display_text="到着",
            data="data not served"
        ),
        styles=BubbleStyle(body=BlockStyle(background_color="#ffffff"))
    ))


if __name__ == "__main__":
    app = Flask(__name__)

    #環境変数取得
    LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
    LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

    line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
    handler = WebhookHandler(LINE_CHANNEL_SECRET)

    @app.route("/callback", methods=['POST'])
    def callback():
        # get X-Line-Signature header value
        signature = request.headers['X-Line-Signature']

        # get request body as text
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)

        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return 'OK'

    @handler.add(MessageEvent)
    def handle_message(event):
        message = arrival_button()
        if message is None:
            return
        line_bot_api.reply_message(
            event.reply_token,
            [arrival_datepicker(), arrival_button()]
        )
    
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

