def bitivektor(n, kombinatsioon):

    if n == 0:
        print(kombinatsioon)

    if n < 0:
        return "1"

    else:
        return bitivektor(n - 1, kombinatsioon + "1")
        return bitivektor(n - 1, kombinatsioon + "1")



bitivektor(5, "")