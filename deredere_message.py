import random

#arrive:到着した人の名前
def yandere_negative(arrive):
	positive_message = ("来てくれたんだ、あなたは私のモノ、頭のてっぺんから、つま先まで、ぜーんぶ、私のモノだよ", "いつもキミのことを見てるよ", "来てくれてありがとう、死んでもキミのことを愛しつづけるよ","やっと来てくれた...さみしいなんて思ってないんだからね!")
	return (arrive + random.choice(positive_message))

if __name__ == "__main__":
	s = "rkun"
	print(yandere_negative(s))