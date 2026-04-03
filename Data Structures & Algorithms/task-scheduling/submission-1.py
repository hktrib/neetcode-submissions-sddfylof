class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        countOfEachTasks = dict()

        maxHeap = []
        q = []

        # Setting the MaxHeap
        for task in tasks:
            if task in countOfEachTasks:
                countOfEachTasks[task] -= 1
            else:
                countOfEachTasks[task] = -1
        
        for key, value in countOfEachTasks.items():
            maxHeap.append([value, key, 0])

        heapq.heapify(maxHeap)

        time = 0
        while maxHeap or q:
            elem = None
            if q and q[0][2] <= time:
                elem = q.pop(0)
                heapq.heappush(maxHeap, elem)
            if maxHeap:
                elem = heapq.heappop(maxHeap)
                elem[0] += 1
                elem[2] = time + n + 1
                if elem[0] < 0:
                    q.append(elem)
            print(f"{time} | {maxHeap} | {q}\n")
            time += 1
        return time
            
            
        


