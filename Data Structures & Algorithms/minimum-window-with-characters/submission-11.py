class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return t
        
        hm = {}
        ans = ""
        l = 0

        for c in t:
            hm[c] = hm.get(c, 0) + 1

        i = len(hm.keys())
        # move r till hm satisfies ref
        for r in range(len(s)):
            if s[r] in hm:
                hm[s[r]] -= 1
                if hm[s[r]] == 0:
                    i -= 1
            
            while l<=r and i==0:
                # move l till hm doesnt satisfy
                if s[l] in hm:
                    if len(s[l:r+1]) < len(ans) or len(ans) == 0:
                        ans = s[l:r+1] 
                    hm[s[l]] += 1
                    if hm[s[l]] > 0:
                        i += 1

                l += 1
  
        return ans


        