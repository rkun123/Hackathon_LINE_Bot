from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, StickerSendMessage, AudioSendMessage, QuickReply, QuickReplyButton, DatetimePickerAction
)

def progress_bar(arrived, member):
	
#	s = "到着率　："
#	rest = member - arrived
#
#	for i in range (arrived):
#		s += "■ "
#	for j in range (rest):
#		s += "□ "
#	s += (" %d人/%d人" % (arrived,member))
	s = (arrived/member )*10	#到着率(0~10)
	if s == 0:
		return ImageSendMessage("https://imgur.com/wB5hFdP")
	elif s == 1:
		return ImageSendMessage("https://imgur.com/exMPWQ6")
	elif s == 2:
		return ImageSendMessage("https://imgur.com/jBh0HqR")
	elif s == 3:
		return ImageSendMessage("https://imgur.com/LV7afnD")
	elif s == 4:
		return ImageSendMessage("https://imgur.com/eVA2ek0")
	elif s == 5:
		return ImageSendMessage("https://imgur.com/VVO8EaF")
	elif s == 6:
		return ImageSendMessage("https://imgur.com/GJU66I0")
	elif s == 7:
		return ImageSendMessage("https://imgur.com/1Q8uqBG")
	elif s == 8:
		return ImageSendMessage("https://imgur.com/eIt9HaS")
	elif s == 9:
		return ImageSendMessage("https://imgur.com/gqXd46i")
	elif s == 10:
		return ImageSendMessage("https://imgur.com/lOU1KYG")
	else:
		return TextSendMessage("Err:Prog_Bar")

if __name__ == "__main__":
	a = 3
	b = 10
	print(progress_bar(a, b))
