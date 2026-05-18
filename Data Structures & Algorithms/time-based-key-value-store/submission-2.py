class TimeMap:

    def __init__(self):
        self.kvStore = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        listForKey = len(self.kvStore[key])
        if listForKey == 0:
            return ""
        else:

            print(f"key: {key} | timestamp: {timestamp}")
            print(f"self.kvStore[key]: {self.kvStore[key]}")
            l = 0
            r = len(self.kvStore[key]) - 1

            # prevL, prevR = -1, -1

            res = ""

            while l <= r:
                m = ((l + r) // 2)
                # print(f"m | {m}")
                mTimeVal = self.kvStore[key][m][0]
                lTimeVal = self.kvStore[key][l][0]
                rTimeVal = self.kvStore[key][r][0]
                prevL, prevR = l, r
                # print(f"prevL | {prevL}")

                # if mTimeVal > lTimeVal and mTimeVal < rTimeVal:
                #     return self.kvStore[key][prevL][1]
                

                if mTimeVal == timestamp:
                    # print(f"mTimeVal == timestamp | {mTimeVal} | {timestamp}")
                    return self.kvStore[key][m][1]
                elif mTimeVal > timestamp:
                    # print(f"mTimeVal > timestamp | {mTimeVal} | {timestamp}")
                    r = m - 1
                elif mTimeVal < timestamp:
                    # print(f"mTimeVal < timestamp | {mTimeVal} | {timestamp}")
                    res = self.kvStore[key][m][1]
                    l = m + 1


            print(f"EDGE CASE l and timestamp: {self.kvStore[key][prevL][0]} | {timestamp}")
            print(f"EDGE CASE r and timestamp: {self.kvStore[key][prevR][0]} | {timestamp}")
            # if self.kvStore[key][prevL][0] < timestamp:
            #     return self.kvStore[key][prevL][1]
            # elif self.kvStore[key][prevR][0] < timestamp:
            #     return self.kvStore[key][prevR][1]
            # else:
            return res
            

                

                
