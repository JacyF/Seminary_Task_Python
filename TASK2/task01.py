# Задача №1:
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, 
# которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# --> 2

coins = int(input("Please, write the quantity of your coins :"))
tail = head = 0
print("Write 1--> if the side is tail ")
print("Write 0--> if the side is head ")

for i in range(coins):
    side = int(input("side of coin ? -->"))
    if side == 1:
        tail += 1
    else:
        head += 1
print('The minimum number of coins to flip is :', tail if tail < head else head, end=' ')
print("So that all the coins are turned up the same")

