import os


def failipuu(faili_nimi, taane):


    if os.path.isfile(faili_nimi):
        print(taane + os.path.basename(faili_nimi))

    else:
       # print(taane + os.path.basename(faili_nimi))
        for i in os.listdir(faili_nimi):
            failipuu(os.path.join(faili_nimi, i), taane + "       ")

failipuu("C:\\Users\\liisi\\PycharmProjects\\Rekursioon", "")
