# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Please introduce a 3 digit number : "))
sum = 0
print(f"---> {number} ")

if ((number > 0) and (number <=999)) :
    while (number != 0) :
        temp = number
        number = number % 10 
        sum = sum + number
        number = temp // 10
    print(f"sum = {sum} <-- ")

else : print("Please introduce a valid number, thanks!!!")