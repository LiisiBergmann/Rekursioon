import os


def faili_suurus(faili_nimi):

    if os.path.isfile(faili_nimi):
        print(os.path.basename(faili_nimi))

    else:

        for a in str(os.path.getsize(faili_nimi)):
            suurem = 0
            list1 = []
            if int(a) > int(suurem):
                list1.append(a)
                print(list1)

        #faili_suurus(os.path.join(faili_nimi + list1)

faili_suurus(("C:\\Users\\liisi\\PycharmProjects\\Rekursioon\\Eelmine aasta"))
