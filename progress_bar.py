

def progress_bar(arrived, member):
	s = "到着率　："
	rest = member - arrived

	for i in range (arrived):
		s += "■ "
	for j in range (rest):
		s += "□ "
	s += (" %d人/%d人" % (a,b))
	return s

if __name__ == "__main__":
	a = 2
	b = 10
	print(progress_bar(a, b))
