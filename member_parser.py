import re

def member_parser(text):
   return re.findall(r'@([A-z0-9!#$%&()=^,./?+*]+)', text)




if __name__ == "__main__":
    print("[ Test ]")
    s = "@rkun!#$%&=^,./?+* @Akira() @akata/? @yuki,."
    print(member_parser(s))
