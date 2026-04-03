class Paran:
    def __init__(self, paranStr="(", openCount=1, closeCount=0):
        self.paranStr = paranStr
        self.openCount = openCount
        self.closeCount = closeCount


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        finalList = []
        stack = []
        stack.append(Paran())

        while stack != []:
            stackTop = stack.pop()

            if len(stackTop.paranStr) == 2*n:
                finalList.append(stackTop.paranStr)
            else:
                if stackTop.openCount == stackTop.closeCount:
                    stack.append(Paran(stackTop.paranStr + "(", stackTop.openCount + 1, stackTop.closeCount))
                else:
                    stack.append(Paran(stackTop.paranStr + ")", stackTop.openCount, stackTop.closeCount + 1))
                    if stackTop.openCount > stackTop.closeCount and stackTop.openCount < n:
                        stack.append(Paran(stackTop.paranStr + "(", stackTop.openCount + 1, stackTop.closeCount))
                         
                
        return finalList