# 18. Zdefiniuj funkcję reverse_str() do odwracania stringu.

def reverse_str(wyrazik):
    wyrazik = (wyrazik[-1:0:-1])
    return wyrazik


if __name__ == '__main__':
    wyraz = "dtiuhgyfufio"
    wyraz = reverse_str(wyraz)
    print(wyraz)
