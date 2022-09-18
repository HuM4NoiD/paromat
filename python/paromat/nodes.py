class Node:
    def __init__(self):
        self.left: Node = None
        self.right: Node = None

    def __repr__(self):
        return f"{self.left} {self.right}"
    
class NumberNode(Node):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return str(self.value)

class OperatorNode(Node):
    def __init__(self, operator: str, left: Node, right: Node):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.operator} {self.right})"

class AddNode(OperatorNode):
    def __init__(self, left, right):
        super().__init__('+', left, right)

class SubtractNode(OperatorNode):
    def __init__(self, left, right):
        super().__init__('-', left, right)

class MultiplyNode(OperatorNode):
    def __init__(self, left, right):
        super().__init__('*', left, right)

class DivideNode(OperatorNode):
    def __init__(self, left, right):
        super().__init__('/', left, right)

class UnaryNode(Node):
    def __init__(self, operator: str, right: NumberNode):
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"{self.operator}{self.right}"

class PlusNode(UnaryNode):
    def __init__(self, right: Node):
        self.operator = '+'
        self.right = right

class MinusNode(UnaryNode):
    def __init__(self, right: Node):
        self.operator = '-'
        self.right = right