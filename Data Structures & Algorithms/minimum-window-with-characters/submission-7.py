class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return t
        
        hm = {}
        ref = {}
        ans = ""
        l = 0
        i = set(t)
        for c in t:
            ref[c] = ref.get(c, 0) + 1
        
        # move r till hm satisfies ref
        for r in range(len(s)):
            if s[r] in ref:
                hm[s[r]] = hm.get(s[r], 0) + 1
                if hm[s[r]] >= ref[s[r]]:
                    i.discard(s[r])
            
            while len(i)==0:
                # move l till hm doesnt satisfy
                if s[l] in hm:
                    if len(s[l:r+1]) < len(ans) or len(ans) == 0:
                        ans = s[l:r+1] 
                    hm[s[l]] -= 1
                    if hm[s[l]] < ref[s[l]]:
                        i.add(s[l])

                l += 1
  
        return ans


        