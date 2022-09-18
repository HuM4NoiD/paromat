from token import Token, Operand, Plus, Minus, Multiply, Divide, OpeningBracket, ClosingBracket
single_tokens = ['+', '-', '*', '/', '(', ')', ' ']
whitespaces = ' \n\t'
digits = '0123456789'

class Lexer():
    def __init__(self, text: str):
        self.text = iter(text)
        self.advance()
    
    def advance(self):
        try:
            self.currentChar = next(self.text)
        except StopIteration:
            self.currentChar = None
    
    def generateTokens(self) -> Token:
        while self.currentChar != None:
            if self.currentChar in whitespaces:
                self.advance()
            elif self.currentChar == '.' or self.currentChar in digits:
                yield self.generateNumber()
            elif self.currentChar == '+':
                self.advance()
                yield Plus()
            elif self.currentChar == '-':
                self.advance()
                yield Minus()
            elif self.currentChar == '*':
                self.advance()
                yield Multiply()
            elif self.currentChar == '/':
                self.advance()
                yield Divide()
            elif self.currentChar == '(':
                self.advance()
                yield OpeningBracket()
            elif self.currentChar == ')':
                self.advance()
                yield ClosingBracket()
            else:
                raise Exception(f"Illegal Character {self.currentChar}")
    
    def generateNumber(self):
        pointCount = 0
        numberString = self.currentChar
        self.advance()

        while self.currentChar != None and (self.currentChar == '.' or self.currentChar in digits):
            if self.currentChar == '.':
                pointCount = pointCount + 1
                if pointCount > 1:
                    break

            numberString = numberString + self.currentChar
            self.advance()
        
        if numberString.startswith('.'):
            numberString = '0' + numberString
        
        if numberString.endswith('.'):
            numberString = numberString + '0'
        
        return Operand(numberString)
