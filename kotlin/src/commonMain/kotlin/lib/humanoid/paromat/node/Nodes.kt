package lib.humanoid.paromat.node

sealed interface Node

class NumberNode(
    val number: Double
): Node {
    override fun toString() = number.toString()
}

sealed class UnaryNode(
    val operator: Char,
    val node: Node
): Node {
    override fun toString() = "$operator($node)"
}

sealed class BinaryNode(
    val left: Node,
    val operator: Char,
    val right: Node
): Node {
    override fun toString() = "$left $operator $right"
}

class PlusNode(node: Node): UnaryNode('+', node)
class MinusNode(node: Node): UnaryNode('-', node)

class AddNode(left: Node, right: Node): BinaryNode(left, '+', right)
class SubtractNode(left: Node, right: Node): BinaryNode(left, '-', right)
class MultiplyNode(left: Node, right: Node): BinaryNode(left, '*', right)
class DivideNode(left: Node, right: Node): BinaryNode(left, '/', right)