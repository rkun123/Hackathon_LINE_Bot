

def progress_bar(arrived, member):
	s = "到着率　："
	per = int(arrived / member* 10)

	for i in range (per):
		s += "■ "
	for j in range (10-per):
		s += "□ "
	s += (" %d人/%d人" % (arrived,member))
	return s

if __name__ == "__main__":
	a = 2
	b = 10
	print(progress_bar(a, b))
