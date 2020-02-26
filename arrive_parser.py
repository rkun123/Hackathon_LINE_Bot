import re

def arrive_parser(event):
    if ('到着' in event["message"]["text"]):
        return event["source"]["userId"]


if __name__ == "__main__":
    print("[ Test ]")
    obj = {"message":{"text":"到着"},"source":{"userId":"U24fe1xxxhogehogexxx"}}
    print(arrive_parser(obj))
