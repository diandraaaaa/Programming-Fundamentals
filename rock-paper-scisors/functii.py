from drawings import rock, paper, scissors


def print1(scor_calculator, scor_jucator):
    if scor_calculator > scor_jucator:
        print('YOU LOST')
    elif scor_calculator < scor_jucator:
        print('YOU WON')
    else:
        print('TIE')


def transforma_din_nr(calculator):
    if calculator == 1:
        calculator = 'rock'
        rock()
    elif calculator == 2:
        calculator = 'paper'
        paper()
    else:
        calculator = 'scissors'
        scissors()
    return calculator