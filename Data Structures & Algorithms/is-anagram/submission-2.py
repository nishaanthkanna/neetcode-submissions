class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramS = {}
        anagramT = {}
        # easy case
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            # compute the occurences
            anagramS[s[i]] = anagramS.get(s[i], 0) + 1
            anagramT[t[i]] = anagramT.get(t[i], 0) + 1
        
        # compare anagramS and anagramT
        for kS, vS in anagramS.items():
            if kS not in anagramT:
                return False

            vT = anagramT[kS]
            if vT != vS:
                return False
        
        return True
            
        