class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = dict()

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        
        print(hm)

        res = []

        for i in range(k):
            print(f"{i}'th iteration")
            largestKey, largestValue = 0, 0
            for key,v in hm.items():
                print(largestKey)
                if v > largestValue:
                    largestKey = key
                    largestValue = v
            res.append(largestKey)
            hm.pop(largestKey)

        return res


                
