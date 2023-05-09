
def listide_järjekord(list1, list2, list3,  kombinatsioon):

    if list1 == [] and list2 == [] and list3 == []:
        print(kombinatsioon)

    else:
        if list1:
            listide_järjekord(list1[1:], list2, list3,  kombinatsioon + list1[0] + " ")
        if list2:
            listide_järjekord(list1, list2[1:], list3,  kombinatsioon + list2[0] + " ")
        if list3:
            listide_järjekord(list1, list2, list3[1:], kombinatsioon + list3[0] + " ")



listide_järjekord(["kas", "mina"], ["olen", "siin"], ["aga", "sina"],  "")