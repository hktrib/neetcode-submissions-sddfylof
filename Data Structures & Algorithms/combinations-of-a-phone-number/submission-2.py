class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Create a Map

        # isolate the different characters and there order
        # and then for each letter possibilty list we append it in its place

        if digits == "":
            return []
            
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backTrack(i, currStr):
            if i >= len(digits):
                res.append(currStr)
                return
            
            for v in digitToChar[digits[i]]:
                backTrack(i + 1, currStr + v)

        
        backTrack(0, "")

        return res