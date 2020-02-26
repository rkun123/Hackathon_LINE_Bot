import re

def member_parser(text):
    # return re.findall(r'^目的地[ 　:]*(.*)$', text)[0]
    return re.findall(r'@([A-z0-9]*)', text)




if __name__ == "__main__":
    print("[ Test ]")
    s = "@rkun20 @Akira @akata @yuki"
    print(member_parser(s))
