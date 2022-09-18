from token import Token, Operand, Plus, Minus, Multiply, Divide, OpeningBracket, ClosingBracket
from nodes import Node, NumberNode, AddNode, SubtractNode, MultiplyNode, DivideNode, PlusNode, MinusNode

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raiseError(self):
        raise Exception("Invalid Syntax")
    
    def advance(self):
        try:
            self.currentToken = next(self.tokens)
        except StopIteration:
            self.currentToken = None
    
    def parse(self):
        if self.currentToken == None: 
            return None

        result = self.expression()

        if self.currentToken != None:
            self.raiseError()

        return result

    def expression(self):
        result = self.term()
        while self.currentToken != None and (isinstance(self.currentToken, Plus) or isinstance(self.currentToken, Minus)):
            if isinstance(self.currentToken, Plus):
                self.advance()
                result = AddNode(result, self.term())
            elif isinstance(self.currentToken, Minus):
                self.advance()
                result = SubtractNode(result, self.term())
        return result


    def term(self):
        result = self.factor()
        while self.currentToken != None and (isinstance(self.currentToken, Multiply) or isinstance(self.currentToken, Divide)):
            if isinstance(self.currentToken, Multiply):
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif isinstance(self.currentToken, Divide):
                self.advance()
                result = DivideNode(result, self.factor())
        return result

    def factor(self):
        token = self.currentToken

        if isinstance(token, OpeningBracket):
            self.advance()
            result = self.expression()
            if not isinstance(self.currentToken, ClosingBracket):
                self.raiseError()

            self.advance()
            return result

        elif isinstance(token, Operand):
            self.advance()
            return NumberNode(token.value)
        elif isinstance(token, Plus):
            self.advance()
            return PlusNode(self.factor())
        elif isinstance(token, Minus):
            self.advance()
            return MinusNode(self.factor())
        
        self.raiseError()
