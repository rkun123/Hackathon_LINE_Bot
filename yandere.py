import random

#noarrive(配列）:未到着の人の名前
def yandere_negative(noarrive):
	i = random.randint(1, 15)
	print (i)
	negative_message = ("時間通りにこないなんて、愛しているの！？愛していないの!?さっさと答えてよっ", "あんたなんか、死んじゃえばいいんだっ！", "もしもし... もしもし...", "生まれてきて、ごめんなさい", "私以外の女といるの？", "こないの？\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nさよなら")
	if i == 1:
		return "縺ゅ＞縺殺∴縺� ス撰ｼ托ｼ抵ｼ殺��ｽゑｽ� �ｸ�ｹ殺ｺ�ｱ�ｲ�ｳ�ｴ�ｵ �ｧ死ｨ�ｩ�ｪ繧ｩ譁�ｭ怜喧縺代ヱ繧ｿ繝ｼ繝ｳ讖溯�繝ｻ遐皮ｩｶ�樞包ｼ搾ｼ�ｿ��｡繹ｱ竭�竇｡"
	else:
		return (random.choice(noarrive) + random.choice(negative_message))



if __name__ == "__main__":
	s = ("rkun", "yuki", "Akira", "akata")
	print(yandere_negative(s))
