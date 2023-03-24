from fractions import Fraction
import sys


class View:

    @classmethod
    def get_number(cls):
        user_number = input('Введите число (комплексное число в формате X+Yj): ')
        try:
            user_number = Fraction(user_number)
            return user_number

        except ValueError:
            try:
                isinstance(complex(user_number), complex)
                return complex(user_number)
            except ValueError:
                print('Неверные данные, завершение работы')
                sys.exit(0)

    @classmethod
    def get_operator(cls):
        action_list = "+-/*"
        while True:
            oper = input('Введите оператор: ')
            if oper in action_list:
                return oper

    @classmethod
    def pprint(cls, text):
        print(text)
