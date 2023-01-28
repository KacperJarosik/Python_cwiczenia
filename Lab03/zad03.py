# 3. Konwersja stopni Celsjusza na Fahrenheita i odwrotnie (funkcja)
#    convert_temp(type, value) gdzie type ma wartości małe lub duże 'F' or 'C'
def convert_temp(type, value):
    if type == 'F' or type == 'f':
        return (value-32)/1.8
    if type == 'C' or type == 'c':
        return (value-32)/(1.8*(value * 9/5) + 32)
x = (input('Podaj typ F/C jednostek temperatury\n'))
y = float(input('Podaj ilosc\n'))
print(convert_temp(x, y))



