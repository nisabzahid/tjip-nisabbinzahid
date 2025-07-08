class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        print(parts)
        stack = []
        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part=="." or part=='':
                continue
            else:
                stack.append(part)
        return  "/"+"/".join(stack)