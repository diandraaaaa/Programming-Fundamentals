lista = [15, 32, 23, 15, 30, 67, 32, 78]

def ex_6():
    rez = []
    aux = []
    index = 0
    for i in range(len(lista)-1):
        if lista[i] % 10 == lista[i+1] // 10:
            aux.append(lista[i])
        else:
            if len(aux) >= len(rez):
                rez = aux
                rez.append(lista[i])
                aux = []
        if len(aux) >= len(rez):
            rez = aux
            index = i
    if lista[index] % 10 == lista[index + 1] // 10:
        aux.append(lista[index+1])
    print(rez)

#ex_6()