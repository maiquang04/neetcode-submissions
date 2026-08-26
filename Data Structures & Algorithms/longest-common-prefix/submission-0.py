class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pf = strs[0]

        for s in strs:
            while not s.startswith(pf):
                pf = pf[:-1]
            if not pf:
                return ""

        return pf