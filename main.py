from utilities.calculator import Calculator

operations = {
    '+': Calculator.sum,
    '-': Calculator.sub,
    '/': Calculator.div,
    '//': Calculator.int_div,
    '%': Calculator.rem,
    '*': Calculator.mul
}

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
command = input('Введите операцию: +, -, /, //, %, *: ').strip()
try:
    print(operations[command](a, b))
except KeyError:
    print('Некорректная команда')
