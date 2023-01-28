results3 = [[float(val) for val in l.split()] for l
            in open("dane.dat","r") if l[0] != "#"]
for i in results3:
    print(i)

print(sum([x[0] for x in results3]))

f = open("dane.dat","a+")
f.write('d')
input('press any key')
f.close()