package lib.humanoid.paromat

import lib.humanoid.paromat.interpreter.Interpreter
import lib.humanoid.paromat.lexer.Lexer
import lib.humanoid.paromat.parser.Parser

class Paromat {

    private val interpreter = Interpreter()

    public fun evaluate(expression: String): Number {
        return interpreter
            .visit(
                Parser(
                    Lexer(expression)
                ).parse()
            )
    }
}