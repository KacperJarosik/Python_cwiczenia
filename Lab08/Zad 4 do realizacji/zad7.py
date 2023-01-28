# 7. Mamy plik tekstowy z danymi medycznymi msk_impact_2017_clinical_data.tsv
# Należy podać ile jest w dnym pliku linii.
if __name__ == '__main__':
    f = open("msk_impact_2017_clinical_data.tsv", 'r')
    licznik = 0
    x = f.readlines()
    print("Liczba linii w pliku: ", len(x))
    f.close()
