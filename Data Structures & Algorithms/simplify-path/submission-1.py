class Solution:
    def simplifyPath(self, path: str) -> str:
        path += "/"
        res = []
        temp = ["/"]

        for c in path:
            if not temp:
                temp.append(c)
                continue
            elif c == "/":
                if temp[-1] == "/":
                    continue
                else:
                    foo = "".join(temp)
                    temp = ["/"]
            else:
                if temp[-1] == "/":
                    foo = "".join(temp)
                    temp = [c]
                else:
                    temp.append(c)
                    continue

            if foo == ".":
                continue
            elif foo == "..":
                if len(res) > 1:
                    res.pop()
                    res.pop()
            elif foo == "/" and res and res[-1] == "/":
                continue
            else:
                res.append(foo)

        while len(res) > 1 and res[-1] == "/":
            res.pop()

        return "".join(res)