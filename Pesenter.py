from Model import Model
from View import View
from logger import logging


class Presenter:

    @classmethod
    def button_click(cls):
        a = View.get_number()
        oper = View.get_operator()
        b = View.get_number()
        res = Model.calculation(a, b, oper)
        result = f'{a}{oper}{b}={res}'
        View.pprint(result)
        logging(result)
