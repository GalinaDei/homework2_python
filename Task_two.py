# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions
import math

a1, b1 = [int(i) for i in input('Введите дробь вида а/в: ').split('/')]
a2, b2 = [int(i) for i in input('Введите вторую дробь вида а/в: ').split('/')]

gdc = math.gcd((a1*b2+a2*b1), b1*b2)
print('Сумма дробей: ', int((a1*b2+a2*b1)/gdc), '/',  int(b1*b2/gdc), sep='')
print('Проверка: ',fractions.Fraction(a1, b1) + fractions.Fraction(a2, b2))
gdc1 = math.gcd(a1*a2, b1*b2)
print('Произведение дробей: ', int((a1*a2)/gdc1), '/',  int(b1*b2/gdc1), sep='')
print('Проверка: ',fractions.Fraction(a1, b1) * fractions.Fraction(a2, b2))

