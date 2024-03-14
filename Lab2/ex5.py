lista = [15, 32, 23, 15, 30, 67, 32, 78]

def ex5():
    aux1 = []
    aux2 = []
    regula = "x+3=y"
    for i in lista:
        regula1 = regula
        regula1 = regula.replace("x", str(i // 10))
        regula1 = regula1.replace("y", str(i % 10))
        aux1, aux2 = regula1.split('=')
        if '+' in aux2:
            e1, e2 = aux2.split('+')
            if int(aux1[0]) == int(e1) + int(e2):
                print(i)
        if '/' in aux2:
            e1, e2 = aux2.split('/')
            if int(aux1[0]) == int(e1) / int(e2):
                print(i)
        if '*' in aux2:
            e1, e2 = aux2.split('*')
            if int(aux1[0]) == int(e1) * int(e2):
                print(i)
        if '-' in aux2:
            e1, e2 = aux2.split('-')
            if int(aux1[0]) == int(e1) - int(e2):
                print(i)
        if '+' in aux1:
            e1, e2 = aux1.split('+')
            if int(aux2[0]) == int(e1) + int(e2):
                print(i)
        if '/' in aux1:
            e1, e2 = aux1.split('/')
            if int(aux2[0]) == int(e1) / int(e2):
                print(i)
        if '*' in aux2:
            e1, e2 = aux1.split('*')
            if int(aux2[0]) == int(e1) * int(e2):
                print(i)
        if '-' in aux1:
            e1, e2 = aux1.split('-')
            if int(aux2[0]) == int(e1) - int(e2):
                print(i)
        if aux1 == aux2:
            print(i)
#ex5()