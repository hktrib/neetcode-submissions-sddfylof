class Solution:

    def checkNumber(self, token) -> bool:
        try:
            float(token)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            match self.checkNumber(token):
                case True:
                    stack.append(int(token))
                case False:
                    print(f"token: {token}")
                    num1 = stack.pop()
                    num2 = stack.pop()
                    print(f"num1: {num1}")
                    print(f"num2: {num2}")
                    if token == '+':
                        stack.append(num2 + num1)
                    elif token == '-':
                        stack.append(num2 - num1)
                    elif token == '*':
                        stack.append(num2 * num1)
                    else:
                        stack.append(int(num2 / num1))

        return stack.pop()