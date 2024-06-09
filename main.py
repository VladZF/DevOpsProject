from utilities.calculator import Calculator
from utilities.work_functions import greeting, sort_array, find_element

operations = {
    '+': Calculator.sum,
    '-': Calculator.sub,
    '/': Calculator.div,
    '//': Calculator.int_div,
    '%': Calculator.rem,
    '*': Calculator.mul,
    '**': Calculator.pow
}


def print_info():
    print('1 - Сгенерировать приветствие')
    print('2 - Отсортировать массив в порядке неубывания')
    print('3 - Найти элемент в массиве')
    print('4 - Выполнить математическую операцию')
    print('5 - Выйти из приложения')


def math_operation():
    command = input('Введите операцию: +, -, /, //, %, *, **, exp: ').strip()
    if command == 'exp':
        x = int(input('Введите показатель степени для e^x: '))
        print(Calculator.exp(x))
    else:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        try:
            print('Результат:', operations[command](a, b))
        except KeyError:
            print('Данная операция не поддерживается')


def main():
    print_info()
    try:
        op = int(input('>>> '))
    except ValueError:
        op = -1
    while op != 5:
        if op == 1:
            name = input('Введите имя: ')
            print(greeting(name))
        elif op == 2:
            arr = [int(x) for x in input('Введите массив: ').split()]
            print('Отсортированный массив:', *sort_array(arr))
        elif op == 3:
            arr = [int(x) for x in input('Введите массив: ').split()]
            target = int(input('Введите элемент, который нужно найти: '))
            index = find_element(arr, target)
            if index == -1:
                print('Искомого элемента нет в массиве')
            else:
                print(f'Элемент находится в массиве под индексом {index}')
        elif op == 4:
            math_operation()
        else:
            print('Некорректная команда')
        try:
            op = int(input('>>> '))
        except ValueError:
            op = -1


if __name__ == '__main__':
    main()
