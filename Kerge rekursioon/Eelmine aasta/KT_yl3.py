# 11. a programmeerimine
# Rekursioon Kontrolltöö
# Nimi : Liisi Bergmann
# Kuupäev : 20.05,2020
# Klass : 11a

# siin selle ülesande point on selles, et sulle on näiteks antud element "a"
# list tähtedega ja mitu korda, see täht kordub

def esineb(element, järjend, kordused):
# siin kontrollitakse, kas kordused on õige kord nagu kordustes ehk selle
# paneme siin siis nulliga võrduma
    if kordused == 0:
        # ja väljastame True
        return True
# kui aga seda elementi järjendis/ehk listis rohkem kui kordusi, või
# vastupidi. Paneme võrduma tühja listi
    if järjend == []:
        # ja väljastame, et see on False
        return False

# siin paneme kohe kindlaks, et järjendi esimene element, kus ta seda lugema hakkab
# on järjendi/listi kohal [0]
    esimene_element = järjend[0]
# siin teeme selgeks, et hakkab kohe lugema enda taga olevaid elemente alates kohal[1]
    ülejäänud = järjend[1:]
# siin kontrollime kas järjendi/ listi element on element mida loeme
    if esimene_element == element:
# kui on siis paneme funktsiooni, elemendi, ülejäänud järjend/list
# ja lahutame ühe korduse maha
        return esineb(element, ülejäänud, kordused - 1)
# kui see kõik ei võrdu mis 29 real siis väljastame lihtsalt funktsioon,
    # ülejäänud listi ja kordused ja ilmselt väljastame siin False
    else:
        return esineb(element, ülejäänud, kordused)

print(esineb("a", ["a","b","a"], 2))
print(esineb("a", ["a","b","a"], 3))