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
import re





def destination_parser(event):
	if event.message.type is "text":
		return re.findall("^[ 　]*([一-龥ぁ-んァ-ンA-z0-9]*)[ 　]*$", event.message.text)[0]
	elif event.message.type is 'location':
		return event.message.address





if __name__ == "__main__":
	app = Flask(__name__)

	#環境変数取得
	LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
	LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

	line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
	handler = WebhookHandler(LINE_CHANNEL_SECRET)

	s = ["rkun", "yuki", "Akira", "akata"]
	
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
		print("てすと")
		print(destination_parser(event))
		message = destination_parser(event)
		line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=message))
	
		print(event)
		print(type(event))
		
	port = int(os.getenv("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
