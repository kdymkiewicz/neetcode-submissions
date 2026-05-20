class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = ["+","-","*","/"]

        for t in tokens:
            print(f"token:{t}")
            if t in operators:
                n1,n2 = s.pop(),s.pop()
                print(f"n1,n2, operator: {n1},{n2},{t}")
                result = int(eval(str(n2)+t+str(n1)))
                print(f"result: {result}")
                s.append(result)
            else:
                print("append")
                s.append(t)
        
        return int(s.pop())