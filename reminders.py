import datetime
from datetime import date
import notify2
import sys

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "create":
            f1 = open('birthdays', 'a')
            f1.write('\n'+input("Enter the date as YYYY MM DD: ")+' ')
            f1.write(input("Enter the name as Dakalti: "))
            f1.close()
        elif sys.argv[1] == "show":
            f1 = open('birthdays','r')
            print (f1.read())
            f1.close()
    else:
        td = date.today()
        f1 = open('birthdays', 'r')
        txt = bdays(f1, td)
        notify2.init("PBR")
        birthday_notification = notify2.Notification(summary = "Happy Birthday to", message = txt, icon = "app_icon.png")
        birthday_notification.show()
        birthday_notification.close()
        f1.close()
    
def bdays(f, today):
    lines = f.readlines()
    txt = ''
    for line in lines:
        l = line.split()
        temp = date(today.year, int(l[1]), int(l[2]))
        age = today.year-int(l[0])
        if temp == today:
            txt = txt + '\n%s, turns %d today, %s' % (l[3], age, temp.strftime('%A, %B %d'))
        elif temp == today + datetime.timedelta(1): 
            txt = txt + '\n%s, turns %d tomorrow, %s' % (l[3], age, temp.strftime('%A, %B %d'))
        elif temp == today + datetime.timedelta(7): 
            txt = txt + '\n%s, turns %d in a week, %s' % (l[3], age, temp.strftime('%A, %B %d'))
    return txt

if __name__ == '__main__':
    main()
