

def naturaalarvud(n, kombinatsioonid):

    if n < 0:
        return

    if n == 0:
        print(kombinatsioonid)

    else:
        naturaalarvud(n-2,kombinatsioonid + [2])
        naturaalarvud(n-1,kombinatsioonid + [1])


print(naturaalarvud(3, []))



def keelatud_mustrid(n, kombinatsioonid):

    if n < 0:
        return

    if n == 0:


        print(kombinatsioonid)

    else:
        keelatud_mustrid(n-2, kombinatsioonid + [2])
        keelatud_mustrid(n-1, kombinatsioonid + [1])


print(keelatud_mustrid(3, []))