# 6. Podaj, w jaki dzień tygodnia urodził się Adam Małysz.
# Data podana może być dowolna. Zdefiniuj funkcję.
import datetime
import calendar

if __name__ == '__main__':
    my_date = datetime.datetime(1977, 12, 3)
    print(calendar.day_name[my_date.weekday()])
