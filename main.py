from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, PostbackEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, StickerSendMessage, AudioSendMessage
)
import os
import random
import re



import session



app = Flask(__name__)

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


sessions = {}


def reply_error(event, message):
    print("[ERROR] "+message)
    line_bot_api.reply_message(event.reply_token, TextSendMessage("[ERROR] " + message))


# get_session return session object by event object
def get_session(event):
    try:
        print(event.source.sender_id)
        # group_id = event["source"]["groupId"]
        group_id = event.source.sender_id
        print("[GROUP_ID] " + group_id)
        try:
            return sessions[group_id]
        except KeyError:
            sessions[group_id] = session.Session(group_id, line_bot_api)
            return sessions[group_id]


    except AttributeError:
        return None
            

def processor(event):
    # departure = departParser(text)
    s = get_session(event)
    if session is None:
        return reply_error(event, "There is no session.")

    return s.execute(event)
    
    # return TextSendMessage(text="It works!!")


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
    print(event)
    print(type(event))
    message = processor(event)
    if message is None:
        return
    line_bot_api.reply_message(
        event.reply_token,
        message
    )

@handler.add(PostbackEvent)
def handle_postback(event):
    print(event)
    message = processor(event)
    if message is None:
        return
    line_bot_api.reply_message(
        event.reply_token,
        message
    )


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
