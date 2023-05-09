

def b(n, k, komb):

    if k == 0 and n == 0:
        print(komb)
        #return komb
    if k < 0 and n < 0:
        return

    else:
        b(k, n - 1, komb + "0")
        b(k-1, n - 1, komb + "1")

print(b(6, 30, ""))