def kuul(tund):
    if tund == 1:
        return 1
    else:
       return kuul(tund-1) * 4
        

print(kuul(3))
