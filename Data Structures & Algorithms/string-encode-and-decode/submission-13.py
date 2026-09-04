class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i, j = 0, 1
        res = []
        while i < len(s):
            while j < len(s) and s[j] != "#":
                j += 1

            length = int(s[i:j])
            end = j + length + 1
            string = s[j+1:end]
            res.append(string)
            i = end
            j = i + 1
        
        return res