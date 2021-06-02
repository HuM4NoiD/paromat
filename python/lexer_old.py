from token import Token, Operand, Plus, Minus, Multiply, Divide, OpeningBracket, ClosingBracket
single_tokens = ['+', '-', '*', '/', '(', ')', ' ']

class UnknownTokenError(Exception):
    pass

def parse(expression) -> list[Token]:
    list: list[Token] = []
    lastToken: Token = Token()
    builder = ''
    for char in expression:
        if char.isdigit() or char == '.':
            builder = builder + char
        elif char in single_tokens:
            if len(builder) > 0:
                list.append(Operand(builder))
                builder = ''
            if char == '+':
                lastToken = Plus()
            elif char == '-':
                lastToken = Minus()
            elif char == '*':
                lastToken = Multiply()
            elif char == '/':
                lastToken = Divide()
            elif char == '(':
                lastToken = OpeningBracket()
            elif char == ')':
                lastToken = ClosingBracket()
            else:
                continue
            list.append(lastToken)
        else:
            raise UnknownTokenError(f"Token not recognized: {char}")
    if len(builder) > 0:
        list.append(Operand(builder))
    return list
                
exp = input(">")
list = parse(exp)
stringed = [str(token) for token in list]
print(stringed)
