from nodes import *
from values import Number

class Interpreter:

    def visit(self, node: Node) -> Number:
        if isinstance(node, NumberNode):
            return self.visitNumberNode(node)
        elif isinstance(node, AddNode):
            return self.visitAddNode(node)
        elif isinstance(node, SubtractNode):
            return self.visitSubtractNode(node)
        elif isinstance(node, MultiplyNode):
            return self.visitMultiplyNode(node)
        elif isinstance(node, DivideNode):
            return self.visitDivideNode(node)
        elif isinstance(node, MinusNode):
            return self.visitMinusNode(node)
        elif isinstance(node, PlusNode):
            return self.visitPlusNode(node)
        else:
            return None

    def visitNumberNode(self, node: NumberNode) -> Number:
        return Number(node.value)
    
    def visitAddNode(self, node: AddNode) -> Number:
        return Number(self.visit(node.left).value + self.visit(node.right).value)

    def visitSubtractNode(self, node: SubtractNode) -> Number:
        return Number(self.visit(node.left).value - self.visit(node.right).value)

    def visitMultiplyNode(self, node: MultiplyNode) -> Number:
        return Number(self.visit(node.left).value * self.visit(node.right).value)

    def visitDivideNode(self, node: DivideNode) -> Number:
        left = self.visit(node.left).value
        right = self.visit(node.right).value
        if right == 0.0:
            raise ZeroDivisionError()
        return Number(self.visit(node.left).value / self.visit(node.right).value)

    def visitMinusNode(self, node: MinusNode) -> Number:
        return Number(-self.visit(node.right).value)

    def visitPlusNode(self, node: PlusNode) -> Number:
        return Number(self.visit(node.right).value)
