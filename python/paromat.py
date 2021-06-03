from lexer import Lexer
from node_parser import Parser
from interpreter import Interpreter

exp = input("> ")
lex = Lexer(exp)
tokens = lex.generateTokens()
parse = Parser(tokens)
parseTree = parse.parse()
if parseTree:
    interpreter = Interpreter()
    result = interpreter.visit(parseTree)
    print(result)