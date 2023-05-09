def järjendite_arv(järjend):

    if järjend == []:
        return 1
    if järjend == 1:
        return 1
    else:
        return järjendite_arv(järjend[1:]) + 1




print(järjendite_arv( [3, [4, [] ], 6] ))