from time import sleep

def stardiloendus(sekundeid_stardini) :
    if sekundeid_stardini == 0:
        print('Start!')
    else:
        print(sekundeid_stardini)
        sleep(1) 
        stardiloendus(sekundeid_stardini-1)
        sleep(1)
        print(sekundeid_stardini)

stardiloendus(3)

