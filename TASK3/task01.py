# Задача 1.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

print('Welcome to this program ')
size = int(input('Introduce the size of matrix --> '))
array = []

for i in range(1, size+1):
    elem = int(input(f'Introduce the {i} element --> '))
    array.append(elem)
print(array)

num = int(input('Introduce a number to see how many time was inserted in matrix : '))
count = 0
for i in range(size):
    if array[i] == num:
        count += 1
print(f' The number {num} was inserted {count} time(s)' if count != 0
      else f'The number {num}, was not inserted')