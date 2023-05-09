list1 = [75, 10, 45, 95, 50, 6, 84, 100]

def mullisorteerimine(list1):

    for i in range(len(list1)):
        for j in range(i):
            if list1[j] < list1[j+1]:
                koht = list1[j]
                list1[j] = list1[j+1]
                list1[j + 1] = koht

print(mullisorteerimine(list1))