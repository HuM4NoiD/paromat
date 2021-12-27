package lib.humanoid.paromat.parser

import lib.humanoid.paromat.node.*
import lib.humanoid.paromat.token.*

class Parser(
    private val tokens: Iterator<Token>
) {

    private var currentToken: Token = Unknown

    init {
        advance()
    }

    private fun advance() {
        currentToken = if (tokens.hasNext()) {
            tokens.next()
        } else {
            Unknown
        }
    }

    public fun parse(): Node {
        if (currentToken == Unknown) {
            throw IllegalStateException("Unknown Token")
        }

        val result = expression()
        if (currentToken != Unknown) {
            throw IllegalStateException("Tokens remain after parsing expression: $currentToken")
        }

        return result
    }

    private fun expression(): Node {
        var result = term()
        while (currentToken != Unknown && (currentToken is Plus || currentToken is Minus)) {
            if (currentToken is Plus) {
                advance()
                result = AddNode(result, term())
            } else if (currentToken is Minus) {
                result = SubtractNode(result, term())
            }
        }
        return result
    }

    private fun term(): Node {
        var result = factor()
        while (currentToken != Unknown && (currentToken is Times || currentToken is By)) {
            if (currentToken is Times) {
                advance()
                result = MultiplyNode(result, term())
            } else if (currentToken is By) {
                result = DivideNode(result, term())
            }
        }
        return result
    }

    private fun factor(): Node {
        return when (val token = currentToken) {
            is OpeningParenthesis -> {
                advance()

                val result = expression()
                if (currentToken !is ClosingParenthesis) {
                    throw IllegalStateException("No Closing Parenthesis succeeding expression $result")
                }
                advance()
                result
            }
            is Operand -> {
                advance()
                NumberNode(token.number)
            }
            is Plus -> {
                advance()
                PlusNode(factor())
            }
            is Minus -> {
                advance()
                MinusNode(factor())
            }
            else -> {
                throw IllegalStateException("Invalid Token for factor")
            }
        }
    }
}