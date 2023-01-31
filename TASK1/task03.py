# Задача 3: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#  Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticket = int(input("Please, introduce the number of ticket with 6 digits : "))
sumfirst3 = 0
sumlast3 = 0

if ((ticket > 0) and (ticket <= 100000)):
    first3dig = ticket // 1000
    last3dig = ticket % 1000

    while (first3dig != 0):
        temp = first3dig
        first3dig = first3dig % 10
        sumfirst3 = sumfirst3 + first3dig
        first3dig = temp // 10

    while (last3dig != 0):
        temp = last3dig
        last3dig = last3dig % 10
        sumlast3 = sumlast3 + last3dig
        last3dig = temp // 10

if (sumfirst3 == sumlast3):
    print(f" Ticket with number {ticket} - Happy ticket ")
else:
    print(f" Ticket with number {ticket} - Unhappy ticket ")
