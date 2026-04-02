class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # find if can make a square
        # pad strings
        n = len(words)
        mx_l = 0
        for s in words:
            mx_l = max(len(s), mx_l)
        if mx_l != n:
            return False
            
        for l, s in enumerate(words):
            if len(s) < n:
                pad = " " * (n-len(s))
                words[l] = words[l] + pad

        for k in range(n):
            for i in range(n):
                if words[k][i] != words[i][k]:
                    return False
        return True
            
        