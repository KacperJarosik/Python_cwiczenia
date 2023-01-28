# 16. Do bieżącej daty dadaj 3 tygodnie lub 21 dni (datetime.timedelta(...))
import datetime

if __name__ == '__main__':
    x = datetime.datetime.now()
    print(x)
    x += datetime.timedelta(21)
    print(x)
