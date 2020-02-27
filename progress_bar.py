from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, StickerSendMessage, AudioSendMessage, QuickReply, QuickReplyButton, DatetimePickerAction, FlexSendMessage, BubbleContainer, BoxComponent, ImageComponent, TextComponent
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
                url = "https://i.imgur.com/wB5hFdP.png"
                return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 1:
		url = "https://i.imgur.com/exMPWQ6.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 2:
		url = "https://i.imgur.com/jBh0HqR.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 3:
		url = "https://i.imgur.com/LV7afnD.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 4:
		url = "https://i.imgur.com/eVA2ek0.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 5:
                url = "https://i.imgur.com/VVO8EaF.png"
                return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 6:
		url = "https://i.imgur.com/GJU66I0.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 7:
		url = "https://i.imgur.com/1Q8uqBG.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 8:
		url = "https://i.imgur.com/eIt9HaS.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 9:
		url = "https://i.imgur.com/gqXd46i.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	elif s == 10:
		url = "https://i.imgur.com/lOU1KYG.png"
		return ImageSendMessage(original_content_url=url, preview_image_url=url)
	else:
		return TextSendMessage("Err:Prog_Bar")

if __name__ == "__main__":
	a = 3
	b = 10
	print(progress_bar(a, b))
