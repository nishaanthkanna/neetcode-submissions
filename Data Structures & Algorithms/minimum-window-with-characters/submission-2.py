class Solution:

    def compare(self, hm: dict, ref: dict) -> bool:
        for k, v in ref.items():
            if hm.get(k, -1) < v:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return t
        
        hm = {}
        ref = {}
        ans = ("", float("inf"))
        l = 0
        r = 0
        i = 0
        for c in t:
            ref[c] = ref.get(c, 0) + 1
            i += 1
        # move r till hm satisfies ref
        for r in range(len(s)):
            if s[r] in ref:
                hm[s[r]] = hm.get(s[r], 0) + 1
            print(self.compare(hm, ref))
            while self.compare(hm, ref) and l <= r:
                # move l till hm doesnt satisfy
                if s[l] in hm:
                    size = len(s[l:r+1])
                    st = s[l:r+1]
                    if size < ans[1]:
                        ans = (st, size) 
                    hm[s[l]] -= 1
                l += 1

            

            
        return ans[0]


        