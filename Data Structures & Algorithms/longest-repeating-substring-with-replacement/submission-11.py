class Solution:

    def checkK(self, hashMap: dict, k: int) -> bool:
        freqList = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        mOC = freqList[0][0]
        for ke, v in hashMap.items():
            if ke != mOC:
                k-= v
        print(mOC)
        return (mOC, k)


    def characterReplacement(self, s: str, k: int) -> int:

        hashMap = {}
        L = 0
        
        max_length = 0
        for R in range(len(s)):
            hashMap[s[R]] = hashMap.get(s[R], 0) + 1
            mOC, kTemp = self.checkK(hashMap, k)

            if kTemp >= 0:
                max_length = max(max_length, R-L+1)
            elif kTemp < 0:
                # increment L pointer
                hashMap[s[L]] -= 1
                L += 1

        return max_length
                

            

                





        