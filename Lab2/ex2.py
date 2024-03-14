lista = [15, 32, 23, 15, 30, 67, 32, 78]

def ex_2():
    p=0
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] % 10 == lista[j]//10 and lista[i]//10 == lista[j] % 10:
                p += 1
    print(p)
ex_2()