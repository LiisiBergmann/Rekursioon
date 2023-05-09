

def kõige_sügavam_koht(element):

    list1 = [0]

    if not isinstance(element, list):
        return

    else:
        for i in element:
            list1.append(kõige_sügavam_koht(i))
        return max(list1) + 1


print(kõige_sügavam_koht( [ [ [ [ ] , [ [ ] ] , [ ]] ] ]))