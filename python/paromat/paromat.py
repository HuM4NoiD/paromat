from cmath import nan
from lexer import Lexer
from node_parser import Parser
from interpreter import Interpreter

def evaluate(expr: str):
    lex = Lexer(expr)
    tokens = lex.generateTokens()
    parser = Parser(tokens)
    parse_tree = parser.parse()
    if parse_tree:
        result = Interpreter().visit(parse_tree)
        return result.value
    else:
        return nan
