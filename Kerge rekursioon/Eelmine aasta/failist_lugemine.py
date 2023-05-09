import os.path

def kuva_failid(kaust, taane):
 #   if (os.path.isdir(kaust))
        for faili_nimi in os.path.isdir(kaust):
            täisnimi = os.path.join(kaust, faili_nimi)
            if (os.path.isdir(täisnimi)):
                print(taane + os.path.basename(faili_nimi))
                kuva_failid(täisnimi, taane,"    ")
            else:
                print(taane + os.path.basename(faili_nimi))

            
        


kuva_failid("This PC:\\Users\\liisi\\PycharmProjects\\Rekursioon", "")