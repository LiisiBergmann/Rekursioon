

def sügavus(element, list):
    list1 = [0]

    if not isinstance(element, list):
        return 0

    else:

        for i in element:
            list1.append(sügavus(i, list))

        return len(list1) + 1

print(sügavus([4,4,2,3[7[7[4]]]],2))