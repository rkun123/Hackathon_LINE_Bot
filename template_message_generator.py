import re, datetime
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, LocationMessage, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction, PostbackAction, FlexSendMessage, BubbleContainer, BubbleStyle, BoxComponent, TextComponent, BlockStyle
)

import os

def arrival_datepicker():
    now_date = datetime.datetime.now().isoformat()
    regex  = re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{2}:[0-9]{2}", now_date)
    tstr = regex[0] + "T" + regex[1]
    # Signatureチェック等
    date_picker = TemplateSendMessage(
        alt_text="予定日を設定",
        template=ButtonsTemplate(
            text="予定日を設定",
            title="集合日時を設定",
            actions=[
                DatetimePickerTemplateAction(
                    label="設定",
                    data="action=buy&itemid=2&mode=datetime",
                    mode="datetime",
                    initial=tstr,
                    min=tstr,
                    max="2099-12-31T23:59"
                )
            ]
        )
    )

    return date_picker

def arrival_button():
    return FlexSendMessage("到着", BubbleContainer(
        size="micro",
        body=BoxComponent(
            layout="vertical",
            contents=[ TextComponent(text="到着したよボタン") ]
        ),
        action=PostbackAction(
            label="到着",
            display_text="到着",
            data="data not served"
        ),
        styles=BubbleStyle(body=BlockStyle(background_color="#7dfffb"))
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
            message
        )
    
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

