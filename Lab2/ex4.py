lista = [15, 32, 23, 15, 30, 67, 32, 78]

def ex_4():
    rez = []
    for i in lista:
        if i == lista[0]:
            rez.append(lista[0])
        else:
            rez.append(i + lista[0])
    print(rez)
#ex_4()
