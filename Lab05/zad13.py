# 13. Zmień sposób wyświetlenia daty tak, aby niedziela była pierwszym dniem tygodnia (calendar.setfirstweekday(6))
# i ponownie wyświetl miesiąc z ważną dla Ciebie datą
import calendar

if __name__ == '__main__':
    calendar.setfirstweekday(6)
    print(calendar.month(2022, 10))
