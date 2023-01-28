#Do dobrych praktyk należy jednak używanie polecenia with przy pracy z plikami. Jego zaletą jest to, że odczytywany plik zostanie poprawnie (automatycznie) zamknięty albo po zakończeniu odczytu, albo po wystąpieniu wyjątku:
#with open('dane.dat') as f:
#	results4 = [[float(val) for val in l.split()] for l in f if l[0] != "#"]
#for i in results4[0:]: print(i)
#Ponieważ plik zostaje otworzony w obrębie bloku rozpoczętego poleceniem with, należy do zasięgu lokalnego. Tuż przed wyjściem z tego bloku interpreter zwalnia zasoby zajęte przez zmienne lokalne, a zatem zamyka również plik.


# wykorzystujemy operator with
with open('dane.dat') as file1:
	results4 = [[float(val) for val in l.split()] for l in file1 if l[0] != "#"]

for i in results4:
    print(i)

#lub to samo
results4 = [[float(val) for val in l.split()] for l in open('dane.dat') if l[0] != "#"]

for i in results4:
    print(i)
