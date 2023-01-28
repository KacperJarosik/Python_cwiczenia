# 4. Zapisujemy do pliku kąt, sinus i consinus z przedziału 0,360 co 1 stopień oraz czytamy te dane.
# przy zapisie stosujemy różne sposoby formatowania łańcucha znaków ( %, .format() oraz f'') ale efekt ma być taki sam.
import math

if __name__ == '__main__':
    f = open("tablice_trygonometryczne.txt", 'w')
    for i in range(361):
        line = "Kat: "
        line += str(i)
        line += " Sinus: "
        line += str(math.sin(i))
        line += " Cosinus: "
        line += str(math.cos(i))
        line += "\n"
        print(line)
        f.write(line)
    f.close()
