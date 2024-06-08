from utilities.calculator import Calculator

operations = {
    '+': Calculator.sum,
    '-': Calculator.sub,
    '/': Calculator.div,
    '//': Calculator.int_div,
    '%': Calculator.rem,
    '*': Calculator.mul,
    '**': Calculator.pow
}

command = input('Введите операцию: +, -, /, //, %, *, **, exp: ').strip()
if command == 'exp':
    x = int(input('Введите показатель степени для e^x: '))
    print(Calculator.exp(x))
else:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    try:
        print(operations[command](a, b))
    except KeyError:
        print('Некорректная команда')
