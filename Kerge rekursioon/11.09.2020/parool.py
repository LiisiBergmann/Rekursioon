
kasutajate_andmed = {"karl.karpov": "1234", "joosep.eelis": "3222","taat.meelis": "1111","kalle.saar": "2322"}


def sisselogimine():
    kasutaja_sisestatud_nimi = input("Sisestage kasutajanimi: ")
    kasutaja_sisestatud_parool = input("Sisestage parool: ")

    if kasutaja_sisestatud_nimi in kasutajate_andmed:
        if kasutajate_andmed[kasutaja_sisestatud_nimi] == kasutaja_sisestatud_parool:
            return
        else:
            sisselogimine()
    else:
        sisselogimine()



sisselogimine()