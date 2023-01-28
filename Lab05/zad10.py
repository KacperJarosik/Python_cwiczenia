# 10. Napisz prosty 'System ekspertowy', który określi czy dana osoba choruje na grypę czy przeziębienie
# w zależności od symptomów. Jeśli mamy wszystkie trzy symptomy: gorączka, ból mieśni
# i osłabienie to mamy grypę. Jeśli mamy gorączkę i osłabienie to przeziębienie,
#  jeśli tylko osłabienie to wszystko OK, a jeśli ból mieśni to jesteśmy przetrenowani.
if __name__ == '__main__':
    print("Odpowiadaj na pytania cyframi \n1 - tak\n0 - nie")
    goraczka = int(input("czy masz gorączkę?\n"))
    bol_miesni = int(input("czy czujesz ból mięśni?\n"))
    oslabienie = int(input("czy czujesz się osłabiony?\n"))
    if oslabienie == 1 and (goraczka == 1 and bol_miesni == 0):
        print("Jesteś przeziębiony")
    elif oslabienie == 1 and (goraczka == 0 and bol_miesni == 0):
        print("Jesteś zdrowy")
    elif oslabienie == 0 and (goraczka == 0 and bol_miesni == 1):
        print("Przetrenowałeś się")
    else:
        print("brak diagnozy")
