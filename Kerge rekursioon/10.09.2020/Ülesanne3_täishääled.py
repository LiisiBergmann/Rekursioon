täehstik = ["a","e","u","i","o","ä","ö","ü","õ"]

def loenda(sõna):
    if sõna == "":
        return sõna
    esimene_element = sõna[0]
    if esimene_element in täehstik:
        return loenda(sõna[1:])

    else:
        return esimene_element + loenda(sõna[1:])




print(loenda("Telefon"))