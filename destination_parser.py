import re

def destination_parser(event):
    return re.findall("^[ 　]*([一-龥ぁ-んァ-ンA-z0-9]*)[ 　]*$", event.message.text)[0]


if __name__ == "__main__":
    s = "  　　とうきょうえき   "

    print(destination_parser({"message": {"text": s}}))
