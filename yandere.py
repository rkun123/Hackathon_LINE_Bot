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

#noarrive(配列）:未到着の人の名前
def yandere_negative(line_bot_api, event, noarrive):
	i = random.randint(1, 30)
	numlist = [6, 7, 8, 9, 16]
	negative_message = ("あんたなんか、死んじゃえばいいんだっ！","私以外の女といるの？", "こないの？\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nさよなら")
	message = ""

	if i == 1:
		message =  "縺ゅ呪＞縺殺∴縺� ス撰ｼ托ｼ抵ｼ殺��ｽゑｽ� �ｸ�ｹ殺ｺ�ｱ�ｲ�ｳ�ｴ�ｵ �ｧ死ｨ�ｩ�呪ｪ繧ｩ譁�ｭ怜喧縺代ヱ繧ｿ呪繝ｼ繝ｳ讖溯�呪繝ｻ遐皮ｩｶ�樞包ｼ搾ｼ�ｿ��｡繹ｱ竭�竇｡"
		line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=message))
	elif 2 <= i and i <= 15:
		#スタンプを送る
		pac = 1
		stic = random.choice(numlist)
		message = StickerSendMessage(
				package_id = pac,
				sticker_id = stic
			)
		for i in range(15):
			line_bot_api.push_message(event.source.sender_id, messages=message)
	else:
		message = random.choice(noarrive) + random.choice(negative_message)
		line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=message))


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
		print(yandere_negative(line_bot_api, event, s))
		print(event)
		print(type(event))
		
	port = int(os.getenv("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
