from lexer import Lexer

exp = input("> ")
lex = Lexer(exp)
tokens = lex.generateTokens()
print(list(tokens))