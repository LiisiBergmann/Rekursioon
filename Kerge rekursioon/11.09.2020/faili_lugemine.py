import os



def failipuu(faili_nimi, taane): #


    if os.path.isfile(faili_nimi):                      # Kas see on fail, siin kontrollime
        print(taane + os.path.basename(faili_nimi))     # saame faili nime ja
                                                        # liidame siia veel taande

    else:
        print(taane + os.path.basename(faili_nimi))
        for i in os.listdir(faili_nimi):                # loob failide nimedest listi aga ta ei loo adresse
                                                        # hakkame faili sisu vaatama
                                                        # ja kasvatame taanet sügavamaks
            failipuu(os.path.join(faili_nimi, i), taane + "       ")

failipuu("C:\\Users\\liisi\\PycharmProjects\\Rekursioon", "")
