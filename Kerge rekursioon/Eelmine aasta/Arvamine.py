
def arva(n):
    
    inimene_kirjutanud = int(input("Sisesta üks number: "))

    if inimene_kirjutanud != n:
        print("Vale, võid uuesti proovida!")

    
    else:
        print("Arvasid ära!")
        arva(n)

arva(50)


