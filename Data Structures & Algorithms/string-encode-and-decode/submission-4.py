class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) >= 1:
            return "$he11$".join(strs)
        else:
            return "$he11$"

    def decode(self, s: str) -> List[str]:
        if s != "$he11$":
            return s.split("$he11$")
        # string is empty 
        else:
            return []