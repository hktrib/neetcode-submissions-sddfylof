class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char != ")" and char != "}" and char != "]":
                stack.append(char)
            else:
                if not stack:
                    return False

                elem = stack[-1]

                match elem:
                    case "(": 
                        if char != ")":
                            return False
                    case "{": 
                        if char != "}":
                            return False
                    case "[": 
                        if char != "]":
                            return False
                stack.pop()

        if len(stack) != 0:
            return False
        
        return True