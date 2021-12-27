package lib.humanoid.paromat.lexer

import lib.humanoid.paromat.token.*

class Lexer(
    val expression: String
): Iterator<Token> {

    private val charIterator = expression.iterator()
    private var currentChar: Char = NULL_CHAR

    init {
        advance()
    }

    private fun advance() {
        currentChar = if (charIterator.hasNext()) {
            charIterator.next()
        } else {
            0.toChar()
        }
    }

    override fun hasNext() = charIterator.hasNext()

    override fun next(): Token {
        if (currentChar != NULL_CHAR) {
            if (currentChar in WHITESPACES) {
                advance()
            } else if (currentChar.isDigit() || currentChar == '.') {
                return generateNumber()
            } else if (currentChar == '+') {
                advance()
                return Plus()
            } else if (currentChar == '-') {
                advance()
                return Minus()
            } else if (currentChar == '*') {
                advance()
                return Times()
            } else if (currentChar == '/') {
                advance()
                return By()
            } else if (currentChar == ')') {
                advance()
                return OpeningParenthesis()
            } else if (currentChar == ')') {
                advance()
                return  ClosingParenthesis()
            }
        }
        throw RuntimeException("Illegal Character found: [$currentChar]")
    }

    private fun generateNumber(): Operand {
        var pointCount = 0;
        val numberBuilder = StringBuilder()

        while (currentChar != NULL_CHAR && currentChar == '.' || currentChar.isDigit()) {
            if (currentChar == '.') {
                ++pointCount
                if (pointCount > 1) {
                    throw IllegalStateException("More than one decimal point for a number in expression")
                }
            }

            numberBuilder.append(currentChar)
            advance()
        }

        val numString = numberBuilder.toString();
        return Operand(numString.toDouble())
    }

    companion object {
        val DIGITS = hashSetOf('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        val WHITESPACES = hashSetOf(' ', '\t', '\n', '\r')
        val SINGLE_SYMBOLS = hashSetOf('+', '-', '*', '/', '(', ')')
        const val NULL_CHAR = 0.toChar()
    }
}