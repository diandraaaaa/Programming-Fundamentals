lista = [15, 32, 23, 15, 30, 67, 32, 78]

def ex_3():
    rez=0
    for i in range(99, 10, -1):
        for j in lista:
            if i == j:
                rez = rez*100+j
    print(rez)
ex_3()