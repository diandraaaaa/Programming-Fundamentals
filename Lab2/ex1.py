lista = [15, 32, 23, 15, 30, 67, 32, 78]
def ex_1():
    freq = {}
    rez= []
    for i in lista:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
        if freq[i] == 1:
            rez.append(i)
    freq[lista[-1]] += 1
    if freq[lista[-1]] > 1:
        lista.remove(i)
    print(rez)
ex_1()