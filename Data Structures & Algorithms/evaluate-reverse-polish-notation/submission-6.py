class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()

                result = int(eval(str(left) + token + str(right)))
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()