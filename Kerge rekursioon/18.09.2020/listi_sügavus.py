

def süavus(element):

    list1 = [0]
    if not isinstance(element, list):
        return 0
    else:

        for i in element:
            list1.append(süavus(i))

        return max(list1) + 1



print(süavus([[[[]]]]))