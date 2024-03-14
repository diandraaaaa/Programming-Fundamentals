"""
citeste desenele din fisier si le printeaza
"""
def rock():
    with open('rock.txt', 'r') as f:
        x = f.read()
    print(x)


def paper():
    with open('paper', 'r') as f:
        x = f.read()
    print(x)


def scissors():
    with open('scissors.txt', 'r') as f:
        x = f.read()
    print(x)


