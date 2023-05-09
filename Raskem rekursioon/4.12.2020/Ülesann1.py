
def bitivektor(n, kombinatsioon):

    if n == 0:
        print(kombinatsioon)
    else:
        # siit hargneb kaheks haruks
        bitivektor(n - 1, kombinatsioon + "0")
        bitivektor(n - 1, kombinatsioon + "1")


bitivektor(7,"")