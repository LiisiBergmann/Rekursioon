täehstik = ["a","e","u","i","o","ä","ö","ü","õ"]

def loenda(sõna):
    if len(sõna) == 0:
        return sõna
    elif sõna[0].lower() not in täehstik:
        return sõna[0] + loenda(sõna[1:])

    else:
        return loenda(sõna[1:])


print(loenda("Telefon"))