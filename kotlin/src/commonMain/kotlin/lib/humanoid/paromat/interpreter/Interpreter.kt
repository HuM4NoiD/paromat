package lib.humanoid.paromat.interpreter

import lib.humanoid.paromat.node.*

class Interpreter: Evaluator<Double> {

    override fun visit(node: Node): Double = when (node) {
        is NumberNode -> visitNumberNode(node)
        is AddNode -> visitAddNode(node)
        is SubtractNode -> visitSubtractNode(node)
        is MultiplyNode -> visitMultiplyNode(node)
        is DivideNode -> visitDivideNode(node)
        is PlusNode -> visitPlusNode(node)
        is MinusNode -> visitMinusNode(node)
    }

    override fun visitNumberNode(node: NumberNode) = node.number

    override fun visitAddNode(node: AddNode) = visit(node.left) + visit(node.right)

    override fun visitSubtractNode(node: SubtractNode) = visit(node.left) - visit(node.right)

    override fun visitMultiplyNode(node: MultiplyNode) = visit(node.left) * visit(node.right)

    override fun visitDivideNode(node: DivideNode) = visit(node.left) / visit(node.right)

    override fun visitPlusNode(node: PlusNode) = visit(node.node)

    override fun visitMinusNode(node: MinusNode) = - visit(node.node)
}