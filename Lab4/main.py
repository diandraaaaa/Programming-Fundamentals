from alfabet import *
from punctuatie import *
from functii import *
import turtle

dictionar = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k, 'L': l, 'M': m,
             'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v, 'W': w, 'X': x, 'Y': y, 'Z': z,
             '.': point}
dict = {}

def scriere_cuvant():
    tur = turtle.Pen()
    cuvant = (input('cuvant = '))
    with open('caractere.txt', 'r') as f:
        simbol = f.read()
    dict = json.loads(simbol)
    for i in cuvant:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.':
            dictionar[i](tur)
        else:
            deseneaza_caracter_definit(tur, i, dict)
    input()

def definire_caracter():
    caracter = input('caracter = ')
    instructiuni = []
    with open('caractere.txt', 'r') as f:
        simbol = f.read()
        dict = json.loads(simbol)
    if caracter in dict:
        return
    deseneaza_carcter(instructiuni)
    dict[caracter] = instructiuni
    with open('caractere.txt', 'w') as f:
        f.write(json.dumps(dict))


def main():
    x = int(input('1. Textnachricht zeichnen 2. Neues Wort hinzufügen'))
    if x == 1:
        scriere_cuvant()
    else:
        definire_caracter()


main()
