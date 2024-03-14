import random

from functii import *

def alegere_calculator():
    calculator = random.randint(1, 3)
    print('computers choice: \n')
    return transforma_din_nr(calculator)


def alegere_jucator():
    x = input('choose rock paper or scissors : ')
    print('your choice: \n ')
    if x == 'rock':
        rock()
    elif x == 'paper':
        paper()
    else:
        scissors()
    return x


def rock_paper_scissors():
    jocuri = 0
    scor_calculator = 0
    scor_jucator = 0
    while jocuri < 3:
        jucator = alegere_jucator()
        calculator = alegere_calculator()
        jocuri += 1
        if calculator == 'rock' and jucator == 'scissors':
            scor_calculator += 1
        if calculator == 'rock' and jucator == 'paper':
            scor_jucator += 1
        if calculator == 'paper' and jucator == 'scissors':
            scor_jucator += 1
        if calculator == 'paper' and jucator == 'rock':
            scor_calculator += 1
        if calculator == 'scissors' and jucator == 'rock':
            scor_jucator += 1
        if calculator == 'scissors' and jucator == 'paper':
            scor_calculator += 1
        print('your score: ', scor_jucator)
        print('computers score: ', scor_calculator)
    print1(scor_calculator, scor_jucator)
rock_paper_scissors()
