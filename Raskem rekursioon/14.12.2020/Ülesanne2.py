
#summa = 13.65
#rahakott = [0.2, 0.5, 1, 2, 0.1, 0.05, 1]

def Juku_rahasumma(rahakott, summa):
    if summa == 0:
        return True

    if summa < 0:
        return False

    if rahakott == []:
        return False

    else:
        return Juku_rahasumma(rahakott[1:], summa - rahakott[0]) or Juku_rahasumma(rahakott[1:], summa)


print(Juku_rahasumma([0.2, 0.5, 1, 2, 0.1, 0.05, 1], 5))