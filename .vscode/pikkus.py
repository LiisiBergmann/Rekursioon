def loenda(elemendi_pikkus):
    if elemendi_pikkus == []:
        return 0

    else:
        return loenda(elemendi_pikkus[1:]) + 1


list = [1,2,3,4,5,6,7,8,9]
print(loenda(list))