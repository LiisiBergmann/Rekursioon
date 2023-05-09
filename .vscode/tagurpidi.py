

def tagurpidi(sõne):

    if sõne == "":
        return sõne
    else:
        esimene_element = sõne[0]
        return tagurpidi(sõne[1:]) + esimene_element



print(tagurpidi("mesi"))