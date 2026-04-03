class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hm = dict()

        # for num in nums:
        #     if num in hm:
        #         hm[num] += 1
        #     else:
        #         hm[num] = 1
        
        # print(hm)

        # res = []

        # for i in range(k):
        #     print(f"{i}'th iteration")
        #     largestKey, largestValue = 0, 0
        #     for key,v in hm.items():
        #         print(largestKey)
        #         if v > largestValue:
        #             largestKey = key
        #             largestValue = v
        #     res.append(largestKey)
        #     hm.pop(largestKey)

        # return res


        hm = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        
        for num, cnt in hm.items():
            freq[cnt].append(num)
        
        # [1, 2, 2, 3, 3, 3]

        # [None, [1], [2, 2], [3,3,3]]
        
        res = [] 
        for i in range(len(freq) -1, -1, -1):
            
            if k == 0:
                print(f"breaking at {i}")
                break
            for f in freq[i]:
                print(f"{freq[i]}")
                res.append(f)
                k -= 1
                if k == 0:
                    print(f"breaking at {i}")
                    break
        return res







