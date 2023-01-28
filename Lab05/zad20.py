# 20. Mamy teskt:
# dane = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, kto cię stracił. Dziś piękność twą w całej ozdobie widzę i opisuję, bo tęsknię po tobie'
# Policz: - ile jest spacji w danym tekście.
#         - ile jest znaków pisanych dużymi literami
#         - ile jest znaków pisanych dużymi literami.
#         - ile jest pozostałych znaków.
# Przekształć tekst na listę, gdzie separatorem elementu jest spacja.
if __name__ == '__main__':
    dane = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, kto cię stracił. Dziś piękność twą w całej ozdobie widzę i opisuję, bo tęsknię po tobie'
    ile_spacji = 0
    ile_duzych_liter = 0
    ile_malych_liter = 0
    ile_inne = 0
    for k in dane:
        if k == " ":
            ile_spacji += 1
        else:
            if 'a' <= k <= 'z':
                ile_duzych_liter += 1
            else:
                if 'A' <= k <= 'Z':
                    ile_malych_liter += 1
                else:
                    ile_inne += 1
    print("Spacji jest: ", ile_spacji, "\n", "Dużych liter jest: ", ile_duzych_liter, "\n", "Małych liter jest: ",
          ile_malych_liter, "\n", "Pozostałych jest: ", ile_inne)
