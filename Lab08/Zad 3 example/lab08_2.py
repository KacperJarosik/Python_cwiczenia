#wypisanie  linii komentarza
f = open("dane.dat","r")
while 1:
    line = f.readline()
    if not line: break
    if line[0] == "#": print(line)
f.close()
