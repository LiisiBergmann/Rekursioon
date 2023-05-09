# 11. a programmeerimine
# Rekursioon Kontrolltöö
# Nimi : Liisi Bergmann
# Kuupäev : 20.05,2020
# Klass : 11a



def sügavus(element):
    list1 = [0]
    # Siin kontrollime, et kui elementi pole listis/ see funktsioon juba tuvastab
    # selle listi ära. Kui pole ühtegi [] listi elementi siis tagastame nulli
    if not isinstance(element, list):
        # isinstance on elemendi andmetüübi testimiseks
        return 0

    else:
        # siin kontrollime ühte elementi elemendis

        for i in element:
            # selle lisame sinna listi, salvestame listi selle funktsiooni elemendi
            # mis luges funktsioonist välja
            list1.append(sügavus(i))
            # siin võtab kogu listi ja liidab neid sinna juurde iga
            # elemendi, mis leiab
        return max(list1) + 1


print(sügavus([[[[[[[]]]]]]]))


