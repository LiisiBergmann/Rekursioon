def bitivektor2(k, n, vektor):

    if (k == 0 and n == 0):
        print(vektor)

    if (k < 0 or n < 0):
        return

    else:
        bitivektor2(k, n-1, vektor + [])
        bitivektor2(k-1, n-1, vektor + [])

print(bitivektor2(4, 2,[]))
