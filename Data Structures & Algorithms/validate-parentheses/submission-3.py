class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s)<2:
            return False

        for c in s:
            if c == '(' or c == "{" or c == "[":
                stack.append(c)
            else:
                if stack:
                    top_c = stack.pop()

                    if (top_c == '(' and c != ')') or (top_c == '{' and c != '}') or (top_c == '[' and c != ']'):
                        return False
                else:
                    return False

        return len(stack) == 0