import random

jack = 10
queen = 10
king = 10
As = 11
talia = [10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7,
         6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
         3, 3, 3, 3, 2, 2, 2, 2, jack, jack, jack,
         jack, queen, queen, queen, queen,
         king, king, king, king, As, As, As, As]


def bet_money():
    while True:
        try:
            bet = int(input('Wpisz jaką kwotę stawiasz:'))
        except:
            print('Musisz wpisać kwotę. Spróbuj jeszcze raz.')
        else:
            print('Dziękuję')
            break
    return bet


class Player():

    def __init__(self, money, suma):
        self.money = money
        self.suma = suma

    def suma_kart(self):
        print(f'Suma wartości kart GRACZA: {self.suma}.')

    def bet_money(self):
        print(f'Graczowi zostało {self.money}zł.')

    def win_money(self):
        self.money = self.money + 2 * bet()

    def __str__(self):
        return f'Gracz ma w tej chwili {self.money}zł'


class Dealer(Player):

    def __init__(self, money, suma):
        super().__init__(money, suma)

    def suma_kart(self):
        print(f'Suma wartości kart BANKU: {self.suma}.')

    def __str__(self):
        return f'W banku jest teraz {self.money}zł'


def bank_start():
    x = random.choice(talia)
    return x


def player_start():
    x = random.choice(talia)
    y = random.choice(talia)
    return x + y


def prompt():
    x = input('Czy chcesz kolejna kartę? Tak//Nie')
    if x.lower() == 'tak':
        y = random.choice(talia)
        print(f'Wylosowałeś {y}')
        return y
    elif x.lower() == 'nie':
        return 0
    else:
        return 0


# Gracz stawia pieniądze
gracz = Player(1000, 0)
bank = Dealer(10000, 0)

while True:
    z = input(
        'Jeżeli chcesz grać wpisz cokolwiek.\nJezeli nie naciśnij enter')
    if z != '':
        bet = bet_money()
        gracz.money = gracz.money-bet
        gracz.bet_money()
        # gracz zaczyna z dwoma kartami
        print('Gracz losuje dwie karty.')
        gracz.suma = player_start()
        gracz.suma_kart()
        # bank losuje
        print('Bank losuje kartę.')
        bank.suma = bank_start()
        bank.suma_kart()
        # gracz kontynuuje
        gracz.suma = gracz.suma + prompt()
        gracz.suma = gracz.suma + prompt()
        gracz.suma_kart()
        # bank losuje 2 kartę
        bank.suma = bank.suma + bank_start()
        bank.suma_kart()

        if bank.suma == 21 or gracz.suma > 21:
            print('PRZEGRAŁEŚ!')
            bank.money = bank.money + bet
        elif gracz.suma == 21 or bank.suma > 21:
            print('WYGRAŁEŚ!')
            gracz.money = gracz.money + 2 * bet
            bank.money = bank.money - bet
        elif bank.suma > gracz.suma:
            print('PRZEGRAŁEŚ!')
            bank.money = bank.money + bet
        elif bank.suma < gracz.suma:
            print('WYGRAŁEŚ!')
            gracz.money = gracz.money + 2 * bet
            bank.money = bank.money - bet
        elif bank.suma == gracz.suma and bank.suma < 22:
            print('REMIS!')
            gracz.money = gracz.money + bet
    else:
        break


print(bank)
print(gracz)
