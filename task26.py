"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """

def summ(a, b):

    if b == 0:
        return a

    return summ(a + 1, b - 1)

summa = summ(int(input('a:')), int(input('b:')))
print(f'sum is {summa}')