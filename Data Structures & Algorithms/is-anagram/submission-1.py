import numpy as np
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        N = len(s)
        S = np.zeros(26)
        T = np.zeros(26)
        # Fill arrays with char occurrences
        for i in range(N):
            cS = ord(s[i]) - 97
            cT = ord(t[i]) - 97
            S[cS] += 1
            T[cT] += 1
        
        if (S==T).all():
            return True
        else:
            return False



        

        