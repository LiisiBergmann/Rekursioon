def suurim(a, b):
    if b == 0:
        print(a)
    else:
        suurim(b, a%b)

suurim(6,2)

