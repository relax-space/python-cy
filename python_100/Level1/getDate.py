# 2.输入日期， 判断这一天是这一年的第几天？

import datetime

def getDate(sDate):
    sDate = sDate.split('.')
    year = int(sDate[0])
    month = int(sDate[1])
    day = int(sDate[2])

    dDate = datetime.date(year = year,month=1,day = 1)
    sDate = datetime.date(year = year,month=month,day = day)
    day = (sDate-dDate).days + 1
    print(day)


if __name__ == "__main__":
    sDate = input('input your date,example:1992.1.1:')
    getDate(sDate)