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
def messages(i):
	list =[]
	if i is "input_destination":
		list = ["待ち合わせ場所を決めましょう、どこにしますか？", "こんどはどこに行きましょう？"]

	elif i is "set_date":
		list = ["目的地は{}だね、集合時間はどうする？", "目的地は{}だね、何時に逢う？", "目的地は{}だね、何時に遭う？"]

	elif i is "invited_person":
		list = ["到着時間は{}だね、私たち以外にだれがくるの？", "到着時間は{}だね、誰が来るの？", "到着時間は{}だね、他に誰かくるの？"]

	elif i is "arrived_user":
		list = ["来てくれたんだ、あなたは私のモノ、頭のてっぺんから、つま先まで、ぜーんぶ、私のモノだよ", "いつもキミのことを見てるよ", "来てくれてありがとう、死んでもキミのことを愛しつづけるよ","やっと来てくれた...さみしいなんて思ってないんだからね!"]
		x = random.randint(1, 3)
		if x == 1:
			list.append("来てくれたんだ、ありが���������� 鐚�鐚�鐚�鐚�鐔�鐔�鐔� 鐚醐執鐚�鐔縁讐鐔鰹輯鐔� 鐔э秀鐔�終����絖��������帥�若��罘��純�紫��腥�鐔���鐚�鐚�鐃�鐃＜�奄����")

	elif i is "unjoined_user_arrived":
		list = ["どちらさまですか？", "{}さん、あなたは呼んでいません", "{}さん、ここは迷子センターではありませんよ", "{}さん、帰ってください"]

	elif i is "duplicated_user_arrived":
		list = ["{}さん、よっぽど私が好きなのね", "{}さん、あなたには飽きたわ", "{}さん、2回到着しないでください", "{}さん、あなたのそういうところが嫌いです", "{}しつこい"]

	return random.choice(list)

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
		print(messages("input_destination"))
		print(messages("set_date"))
		print(messages("invited_person"))
		print(messages("arrived_user"))
		print(messages("unjoined_user_arrived"))
		print(messages("duplicated_user_arrived"))
		print(messages("delay_user"))

		#line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=messages("input_destination")))
		#line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=messages("set_date")))
		#line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=messages("invited_person")))
		#line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=messages("arrived_user")))
		#line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=messages("unjoined_user_arrived")))
		#line_bot_api.push_message(event.source.sender_id, messages=TextSendMessage(text=messages("duplicated_user_arrived")))

	
		print(event)
		print(type(event))
		
	port = int(os.getenv("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
