
def bitivektor(n, kombinatsioon):

    if n == 0:
        print(kombinatsioon)



    else:
        print(kombinatsioon)
        # siit hargneb kaheks haruks
        bitivektor(n - 1, kombinatsioon + "0")
        bitivektor(n - 1, kombinatsioon + "1")


bitivektor(3,"")