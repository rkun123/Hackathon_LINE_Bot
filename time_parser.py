import re
import datetime

def time_parser(event):
    regex = re.findall(r'[0-9]{4}|[0-9]{2}-[0-9]{2}|[0-9]{2}:[0-9]{2}', event)
    if(len(regex)==3):
        str = regex[0] + '-' + regex[1] + ' ' + regex[2]
    elif(len(regex)==2):
        str = datetime.date.today().strftime('%Y') + '-' + regex[0] + ' ' + regex[1]
    elif(len(regex)==1):
        str = datetime.date.today().strftime('%Y') + '-' + datetime.date.today().strftime('%m-%d') +' ' + regex[0]
    date = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M')
    return date

def remain_time(event):
    return  datetime.datetime.now() - event

if __name__ == "__main__":
    s = "2020-02-26 14:42"
    print(time_parser(s))
    s = "02-20 14:42"
    print(time_parser(s))
    s = "14:42"
    print(time_parser(s))
    print(remain_time(time_parser(s)))
