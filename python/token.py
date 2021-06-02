class Token:
    def __init__(self):
        pass

class Grouper(Token):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"[{self.__class__.__name__}: {self.value}]"

class OpeningBracket(Grouper):
    def __init__(self):
        super().__init__('(')

    def __str__(self):
        return str(self.value)

class ClosingBracket(Grouper):
    def __init__(self):
        super().__init__(')')

    def __str__(self):
        return str(self.value)


class Operator(Token):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def precedence(self):
        return 0

    def __repr__(self):
        return f"[{self.__class__.__name__}: {self.value}]"

class Operand(Token):
    def __init__(self, value: str):
        super().__init__()
        if value.startswith('.'):
            value = '0' + value
        self.value = float(value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"[{self.__class__.__name__}: {self.value}]"

class Plus(Operator):
    def __init__(self):
        super().__init__('+')

    def __str__(self):
        return str(self.value)

    def precedence(self):
        return 1

class Minus(Operator):
    def __init__(self):
        super().__init__('-')

    def __str__(self):
        return str(self.value)

    def precedence(self):
        return 1

class Multiply(Operator):
    def __init__(self):
        super().__init__('*')

    def __str__(self):
        return str(self.value)

    def precedence(self):
        return 2

class Divide(Operator):
    def __init__(self):
        super().__init__('/')

    def __str__(self):
        return str(self.value)

    def precedence(self):
        return 2
