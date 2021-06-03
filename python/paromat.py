from lexer import Lexer
from node_parser import Parser

exp = input("> ")
lex = Lexer(exp)
tokens = lex.generateTokens()
parse = Parser(tokens)
print(parse.parse())