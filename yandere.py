import random

#noarrive(配列）:未到着の人の名前
def yandere_negative(noarrive):
	negative_message = ("時間通りにこないなんて、愛しているの！？愛していないの!?さっさと答えてよっ", "あんたなんか、死んじゃえばいいんだっ！", "もしもし... もしもし...", "生まれてきて、ごめんなさい")

	return (random.choice(noarrive) + random.choice(negative_message))




if __name__ == "__main__":
	s = ("rkun", "yuki", "Akira", "akata")
	print(yandere_negative(s))
