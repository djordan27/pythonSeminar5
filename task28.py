"""Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4 
    """
def power(num1, num2):
    if num2 == 0:
        return 1

    return num1 * power(num1, num2 - 1)


num = power(int(input('number: ')), int(input('degree: ')))
print(f'number is {num}')