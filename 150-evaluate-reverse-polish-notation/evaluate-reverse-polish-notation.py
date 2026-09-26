class Solution:
    def evalRPN(self, tokens: list[str]) -> int:


        stack = []

        for token in tokens:

            if token == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(first) + int(second))
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) - int(first))
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(first) * int(second))
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) / int(first))
            else:
                stack.append(token)


        return int(stack[0])