class Node:
    def __init__(self):
        self.left: Node = None
        self.right: Node = None
    
class NumberNode(Node):
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return str(self.value)

class OperatorNode(Node):
    def __init__(self, operator: str):
        self.operator = operator

    def __repr__(self):
        return f"({self.left} {self.operator} {self.right})"

class AddNode(OperatorNode):
    def __init__(self):
        super().__init__('+')

class SubtractNode(OperatorNode):
    def __init__(self):
        super().__init__('-')

class MultiplyNode(OperatorNode):
    def __init__(self):
        super().__init__('*')

class DivideNode(OperatorNode):
    def __init__(self):
        super().__init__('/')