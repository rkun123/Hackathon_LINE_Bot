import re

def member_parser(event):
   return re.findall("(@[一-龥ぁ-んァ-ンA-z0-9 ]+[一-龥ぁ-んァ-ンA-z0-9])\ *", event.message.text)




if __name__ == "__main__":
    print("[ Test ]")
    s = "@rkun!#$%&=^,./?+* @Akira() @akata/? @yuki,."
    print(member_parser(s))
