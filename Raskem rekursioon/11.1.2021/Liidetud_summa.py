def summa(list1):

    if not list1:
        return 0

    else:
        return list1[0] + summa(list1[1:])


print(summa([1, 20, 45, -1, 1]))