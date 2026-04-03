class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = dict()

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        
        sorted_hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))

        i = 0

        ret = []

        print(sorted_hm)

        for key,v in sorted_hm.items():
            print(f"k: {key} | {i} | {k}")
            if i == k:
                break
            ret.append(key)
            i += 1
        
        return ret