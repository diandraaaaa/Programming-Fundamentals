import json
import turtle


def deseneaza_caracter_definit(tur, i, dict):
    """  functia parcurge instructiunile din lista
        din fisierul caractere """
    tur.left(90)
    for j in dict[i]:
        if j == 'w':
            tur.forward(10)
        if j == 's':
            tur.backward(10)
        if j == 'a':
            tur.left(45)
        if j == 'd':
            tur.right(45)
        if j == 'f':
            tur.up()
        if j == 'g':
            tur.down()


def transformare_lista_in_dictionar():
    """
    transforma lista din carctere.txt intr-un dictionar
    """
    with open('caractere.txt', 'r') as f:
        simbol = f.read()
    dict = json.loads(simbol)
    return dict

def transformare_dictionar_in_lista():
    """
    scrie in document instructiunile date de utilizator sub forma unei liste
    """
    with open('caractere.txt', 'w') as f:
        f.write(json.dumps(dict))
def deseneaza_carcter(instructiuni):
    """
    deseneaza ce vrea utilizatoru
    """
    turtle.setup(500, 500)
    turtle.setheading(90)
    turtle.speed(0)

    def up():
        turtle.forward(10)
        instructiuni.append('w')

    def down():
        turtle.backward(10)
        instructiuni.append('s')

    def left():
        turtle.left(45)
        instructiuni.append('a')

    def right():
        turtle.right(45)
        instructiuni.append('d')

    def stop():
        turtle.up()
        instructiuni.append('f')

    def start():
        turtle.down()
        instructiuni.append('g')

    turtle.listen()
    turtle.onkey(up, 'w')
    turtle.onkey(down, 's')
    turtle.onkey(left, 'a')
    turtle.onkey(right, 'd')
    turtle.onkey(stop, 'f')
    turtle.onkey(start, 'g')
    turtle.onkey(turtle.bye, 'Return')

    turtle.mainloop()

