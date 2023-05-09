
list = [0,1]
def fib(n):
    if (len(list)-1) >= n:
        return list[n]
    else:
        arv = fib(n-1)+fib(n-2)
        list.append(arv)
        return arv


print(fib(5))