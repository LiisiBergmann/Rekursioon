

def loo_list(tase):
    list = []
    if tase == 1:
        return list

    else:
        list.append(loo_list(tase - 1))
        return list

print(loo_list(4))