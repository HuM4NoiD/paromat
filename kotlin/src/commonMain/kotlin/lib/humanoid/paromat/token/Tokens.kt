package lib.humanoid.paromat.token

sealed interface Token

object Unknown: Token

public sealed class Operator(val operator: Char): Token
public class Operand(val number: Double): Token
public sealed class Parenthesis(val symbol: Char): Token

public class Plus: Operator('+')
public class Minus: Operator('-')
public class Times: Operator('*')
public class By: Operator('/')

public class OpeningParenthesis: Parenthesis('(')
public class ClosingParenthesis: Parenthesis(')')
