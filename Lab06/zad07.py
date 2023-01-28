# 7. Ile aktualnie lat ma Adam Małysz (albo dowolna osoba).
# Zdefiniuj funkcję how_old(date).
import datetime


def how_old(date):
    now = datetime.datetime.now()
    rok1 = now.year
    rok2 = date.year
    return rok1 - rok2


if __name__ == '__main__':
    print(how_old(datetime.datetime(1977, 12, 3)))
