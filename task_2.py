# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random
n = int(input('Введите кол-во оценок '))
sp = [random.randint(1,5) for i in range(n)]
print(sp)

a = max(sp)
b = min(sp)

for i in range(n):
    if sp[i] == a:
        sp[i] = b
print(sp)