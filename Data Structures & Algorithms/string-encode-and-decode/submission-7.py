class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        # check for ""
        output = []
        for s in strs:
            output.append(f"#{len(s):03d}{s}")
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        output = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                # fixed 3 digit length
                length = int(s[i+1:i+4])
                output.append(s[i+4:i+4+length])
                i = i+4+length
        
        return output
