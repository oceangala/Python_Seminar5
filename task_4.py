# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def input_int():
    while True:
        number = input('Введите число: ')
        try:
            return int(number)
        except:
            print('Это не число. Повторите ввод')

print(input_int())
st = input('Введите последовательность: ')
print(st[::-1])
