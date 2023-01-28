# Zadanie 13. (do przeanalizowania)
# Zmodyfikuj zadanie 11 tak, żeby
# - polskie adresy zostały zapisane do pliku webs_pl.txt a pozostałe adresy do pliku webs_other.txt
# nowe pliki mają powstać w tym samym katalogu co wejściowy plik wskazany przez użytkownika (skorzystaj z funkcji os.path.dirname)
# -zapisując linie do plików dodawaj do nich znak nowej linii

#-------------------------------------------------------------------------------------------
import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')
filePL = open(websPathPL,'w')
fileOther = open(websPathOther,'w')
for line in webaddresses:
    if line.endswith('.pl'):
        filePL.write(line+"\n")
    else:
        fileOther.write(line+"\n")
filePL.close()
fileOther.close()
