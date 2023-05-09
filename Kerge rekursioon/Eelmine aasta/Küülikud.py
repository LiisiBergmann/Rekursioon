
def küülik(kuud):

    if kuud == 0:
        return 1

    elif kuud == 1:
        return 1

    else:
        return küülik(kuud-1) + küülik(kuud-2)

    
print(küülik(6))
