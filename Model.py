class Model:

    a = None
    b = None
    operator = None

    @classmethod
    def calculation(cls, a, b, operator):
        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y}

        result = operators[operator](a, b)
        return result
