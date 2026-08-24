class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
            }

        for token in tokens:
            if token in operands:
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(operands[token](y, x))
            else:
                stack.append(token)

        return int(stack.pop())