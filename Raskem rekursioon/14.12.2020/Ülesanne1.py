
hulk = [1,2,3,4]

def alamhulgad(hulk, alamhulk : list):
    #list on tühjaks tehtud,
    # siis prindime selle alamhulgad välja

    if hulk == []:
        print(alamhulk)

    else:
        alamhulgad(hulk[1:], alamhulk + [hulk[0]])
        alamhulgad(hulk[1:], alamhulk)


alamhulgad(hulk, [])