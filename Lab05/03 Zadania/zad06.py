# 6. Wykorzystaj moduł datetime do podania w osobnych linijkach roku, miesiąca, dnia
#    oraz godziny, minuty i sekundy w danym momencie.
import datetime
today = datetime.datetime.now()
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)