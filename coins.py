import random


class Coin:
    """Класс монетка

    Атрибуты:
     side- сторона heads-орел/tails-решка
    """
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.choice(['heads','tails'])


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

n = int(input('Введите количество монет: '))

coins=[]
#создаём и подбрасываем монетки
for i in range(n):
    coins.append(Coin())


#вычисляем соотношения
heads_cnt=0
tails_cnt=0

for coin in coins:
    coin.flip()
    if coin.side=='heads':
        heads_cnt+=1
    if coin.side=='tails':
        tails_cnt+=1

heads_prcnt=heads_cnt/len(coins)*100
tails_prcnt=tails_cnt/len(coins)*100

print(f"процент выпадания олов ({heads_cnt} раз) итераций:{heads_prcnt}")
print(f"процент выпадания решек из ({tails_cnt} раз) итераций:{tails_prcnt}")
