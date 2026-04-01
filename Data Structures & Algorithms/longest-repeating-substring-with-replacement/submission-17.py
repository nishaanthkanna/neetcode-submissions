class Solution:


    def calcmOC(self, hashMap: dict) -> ([str, int], int):
        tempMOC = ["a", 0]
        otherOcc = 0
        for c, f in hashMap.items():
            if tempMOC[1] < f:
                tempMOC = [c, f]
            otherOcc += f
        otherOcc -= tempMOC[1]
        return tempMOC, otherOcc



    def characterReplacement(self, s: str, k: int) -> int:

        hashMap = {}
        L = 0
        mOC = [s[0], 0]
        otherOcc = 0
        max_length = 0
        for R in range(len(s)):
            print(mOC)
            print(otherOcc)
            hashMap[s[R]] = hashMap.get(s[R], 0) + 1
            mOC, otherOcc  = self.calcmOC(hashMap)

            kTemp = k - otherOcc

            if kTemp >= 0:
                max_length = max(max_length, R-L+1)
            elif kTemp < 0:
                # increment L pointer
                hashMap[s[L]] -= 1
                mOC, otherOcc  = self.calcmOC(hashMap)
                L += 1

        return max_length
                

            

                





        