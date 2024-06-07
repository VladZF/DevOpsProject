class Calculator:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'Не определено'

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def int_div(a, b):
        try:
            return a // b
        except ZeroDivisionError:
            return 'Не определено'

    @staticmethod
    def rem(a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return 'Не определено'
