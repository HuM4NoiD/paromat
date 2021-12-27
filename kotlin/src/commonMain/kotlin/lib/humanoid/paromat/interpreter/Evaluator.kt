package lib.humanoid.paromat.interpreter

import lib.humanoid.paromat.node.*

interface Evaluator<Result> {

    fun visit(node: Node): Result

    fun visitNumberNode(node: NumberNode): Result

    fun visitAddNode(node: AddNode): Result

    fun visitSubtractNode(node: SubtractNode): Result

    fun visitMultiplyNode(node: MultiplyNode): Result

    fun visitDivideNode(node: DivideNode): Result

    fun visitPlusNode(node: PlusNode): Result

    fun visitMinusNode(node: MinusNode): Result
}