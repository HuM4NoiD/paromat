from token import Token

class Node:
    def __init__(self, token: Token):
        self.token = token
        self.left = None
        self.right = None
    