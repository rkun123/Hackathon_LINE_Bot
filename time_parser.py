import re
import datetime

def time_parser(event):
    regex = re.findall(r'[0-9]{4}|[0-9]{2}-[0-9]{2}|[0-9]{2}:[0-9]{2}', event.datetime)
    if(len(regex)==3):
        str = regex[0] + '-' + regex[1] + ' ' + regex[2]
    date = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M')
    return date

def remain_time(event):
    return  event - datetime.datetime.now()

if __name__ == "__main__":
    s = "2020-02-26T21:17"
    print(time_parser(s))
    print(remain_time(time_parser(s)))
