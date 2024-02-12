# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input('Введите целое число: '))


def convert_to_hexadecimal(num):
    hexadecimal_digits ='0123456789ABCDEF'
    hexadecimal = ''
    while num > 0:
        index = num % 16
        hexadec_dig = hexadecimal_digits[index]
        hexadecimal += hexadec_dig
        num //= 16
    return ''.join(reversed(hexadecimal))


print(convert_to_hexadecimal(number))


print(hex(number))
