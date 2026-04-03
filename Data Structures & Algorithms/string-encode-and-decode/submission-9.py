class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        if strs == [""]:
            return "|"

        # print("|".join(strs))
        return "|".join(strs)

    def decode(self, s: str) -> List[str]:

        print(f"s: {s}")
        if s == "":
            return []

        if len(s) == 1:
            return [""]

        tmpStr = ""
        strList = []

        for char in s:
            # print(char)

            if char == "|":
                # print(f"tmpStr: {tmpStr}")
                # print(f"strList: {strList}")
                strList.append(tmpStr)
                tmpStr = ""
            else:
                tmpStr += char

        strList.append(tmpStr)
        return strList
