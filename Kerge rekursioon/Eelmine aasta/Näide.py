def funktsioon(n):
    for n in range(n):
        print(n)
        n -= 1

funktsioon(5)


def funktsioon2(n):
    if n == 0:
        return
    
    else:
        print(n)
        funktsioon2(n-1)

funktsioon2(5)