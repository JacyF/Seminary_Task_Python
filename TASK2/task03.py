# Задача №2:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3


s = int(input("Whats the result of their summ ? ---> "))
p = int(input("Whats the result of their multiplication ? ---> "))

control = n1 = 0

for i in range(1, p):
    if p / i == s - i:
        control += 1 
        n1 = s - i
if (n1 or s - n1) <= 1000:
    print(f' The numbers are {n1} and {s - n1} ' if control != 0 else "The numbers dont match" )
else:
    print("Please choose numbers smaller or iqual 1000 ")
