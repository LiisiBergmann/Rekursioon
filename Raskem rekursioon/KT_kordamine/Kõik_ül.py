
def kolmNeliViis(n, komb : list):

    if (n == 0):
        print(komb)
        return 1

    if n < 0:
        return 0

    else:
        return kolmNeliViis(n - 3, komb + [3]) + kolmNeliViis(n - 4, komb + [4])+ kolmNeliViis(n - 5, komb + [5])

#kolmNeliViis(12,[])

def bitivektor2(k, n, vektor):

    if (k == 0 and n == 0):
        print(vektor)

    if (k < 0 or n < 0):
        return

    else:
        bitivektor2(k, n-1, vektor + "0")
        bitivektor2(k-1, n-1, vektor + "1")

print(bitivektor2(4, 2,[]))

juhuRahakott = [0.2, 1, 2, 1, 0.5, 0.2, 2, 0.1, 2, 0.05]
summa = 5.75

def jukuYl(järjend, summa):

    if summa == 0:
        return True

    if järjend == []:
        return False

    if summa < 0:
        return False

    else:
        return (jukuYl(järjend[1:], round(summa - järjend[0], 2)) or jukuYl(järjend[1:], summa))
#print(jukuYl(juhuRahakott, summa))



# kuni viis
def komb_1ja2(n, komb):
    if n < 0:
        return
    if n == 0:
        print(komb)
    else:
        komb_1ja2(n-2, komb+ [2])
        komb_1ja2(n-1, komb+ [1])


komb_1ja2(5, [])


def tooted(toodetelist, summa):

    if summa > 100:
        return 0

    if summa <= 100:
        return summa

    else:
        max(tooted(toodetelist[1:], summa), max(tooted(toodetelist[1:], summa + toodetelist[0]*2), tooted(toodetelist[1:], summa + toodetelist[0])))




