

def auto_hind(hind, aasta):
    if aasta == 0:
        return hind


    else:
        return round(auto_hind(hind * 0.8, aasta - 1), 2)




print(auto_hind(10000.0, 0))
print(auto_hind(10000.0, 5))
print(auto_hind(10000.0, 1))
print(auto_hind(10000.0, 6))