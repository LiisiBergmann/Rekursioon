

def Lineaarne_otsing(a,alg,lopp):

    for i in range(alg,lopp+1):
        mini = i
        for j in range(i, lopp+1):
            if a[j] < poolitus_meetod:
                mini = j
                a[i], a[mini] = a[mini], a[i]
    return a
print(Lineaarne_otsing([75, 10, 45, 95, 50, 6, 84, 100], 10, 100))

def poolitus_meetod(list1):

    for i in range(len(list1)):
        for n in range(i):
            if i > n:
                koht = list1[n]
                list1[n] = list1[n+1]
                list1[n+1] = koht

    return koht

print(poolitus_meetod([75, 10, 45, 95, 50, 6, 84, 100], 10, 100))

def topeltpoolitus(alg, lõpp, r):

    if lõpp < r:
        kohal = alg[lõpp]
        i = lõpp+1
        j = r
        while i < j:
            while alg[i] <= kohal and i < r:
                i += 1
                while alg[j] > kohal and j > lõpp:
                    j -= 1
                    if i < j:
                            abi=alg[i]
                            alg[i]=alg[j]
                            alg[j]=abi
                            if kohal > alg[j]:
                                alg[lõpp] = alg[j]
                                alg[j] = kohal
                                topeltpoolitus(alg,lõpp,j-1)
                                topeltpoolitus(alg,i,r)

print(topeltpoolitus(10, 100, [75, 10, 45, 95, 50, 6, 84, 100]))