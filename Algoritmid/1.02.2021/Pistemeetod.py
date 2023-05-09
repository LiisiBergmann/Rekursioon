list1 = [75, 10, 45, 95, 50, 6, 84, 100]


def pistemeetod(list1):

    for i in range(len(list1)):
        for n in range(i):
            if i > n:
                koht = list1[n]
                list1[n] = list1[n+1]
                list1[n+1] = koht

    return koht

print(pistemeetod(list1))