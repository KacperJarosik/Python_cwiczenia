# 8. Podaj ile dni upłyneło od 1.01.2000 roku do aktualnej daty
import datetime

if __name__ == '__main__':
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    x = (datetime.datetime(year, month, day) - datetime.datetime(2000, 1, 1))
    print(x)
