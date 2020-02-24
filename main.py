from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, StickerSendMessage, AudioSendMessage
)
import os
import random

app = Flask(__name__)

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# hands_to_int
def hands_to_int(userhand):
    if userhand == "グー":
        return 0
    elif userhand == "チョキ":
        return 1
    elif userhand == "パー":
        return 2
    else:
        return -1

def select_bothand():
   return random.randint(0, 2)

def judge(userhand, bothand):
    if userhand == -1:
        return "Select by グー/チョキー/パー"

    if bothand == 0:
        hand = "グー"
    elif bothand == 1:
        hand = "チョキ"
    else:
        hand = "パー"
 
    if (userhand - bothand + 3) % 3 == 0:
        message = StickerSendMessage(
            package_id = 1,
            sticker_id = 1
        )	    
        return message
    elif (userhand - bothand + 3) % 3 == 1:
        message = AudioSendMessage(
            original_content_url = "https://hanson1.herokuapp.com/static/audios/se_maoudamashii_onepoint33.mp3",
            duration = 1000
        )
        return message
    else:
        message = ImageSendMessage(
            original_content_url = "https://hanson1.herokuapp.com/static/images/index.jpeg", 
            preview_image_url = "https://hanson1.herokuapp.com/static/images/index.jpeg"
        )
        return message
    return TextSendMessage(text="bothand is " + hand + "\n" + text)

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = judge(hands_to_int(event.message.text), select_bothand())
    line_bot_api.reply_message(
        event.reply_token,
        message
    )

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
