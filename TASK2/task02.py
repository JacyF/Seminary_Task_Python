# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
#  не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input("Write a number : "))
for i in range(number):
    if 2 ** i <= number:
        print(2 ** i)
    else:
        break
