class Token:
    def __init__(self):
        pass

class Grouper(Token):
    def __init__(self, value):
        self.value = value

class OpeningBracket(Token):
    def __init__(self):
        super().__init__('(')

    def __str__(self):
        return str(self.value)

class ClosingBracket(Token):
    def __init__(self):
        super().__init__(')')

    def __str__(self):
        return str(self.value)


class Operator(Token):
    def __init__(self, value):
        super().__init__()
        self.value = value

class Operand(Token):
    def __init__(self, value: str):
        super().__init__()
        if value.startswith('.'):
            value = '0' + value
        self.value = value

    def __str__(self):
        return str(self.value)

class Plus(Operator):
    def __init__(self):
        super().__init__('+')

    def __str__(self):
        return str(self.value)

class Minus(Operator):
    def __init__(self):
        super().__init__('-')

    def __str__(self):
        return str(self.value)

class Multiply(Operator):
    def __init__(self):
        super().__init__('*')

    def __str__(self):
        return str(self.value)

class Divide(Operator):
    def __init__(self):
        super().__init__('/')

    def __str__(self):
        return str(self.value)
