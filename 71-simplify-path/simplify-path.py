class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        st = [""]

        for k in arr:
            if k == "" or k == ".":
                continue
            if k == ".." and len(st) == 0:
                continue
            if k == "..":
                st.pop(-1)
                continue
            st.append(k)
        print(st)
        if len(st) > 0 and st[0] != "":
            st = [""] + st
        if len(st) == 1:
            return "/" # still just one element 
        return "/".join(st) if len(st) > 0  else "/"
            
        