class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        hs = {}
        for k in allowed:
            if k[0:2] not in hs:
                hs[k[0:2]] = []
            hs[k[0:2]].append(k[2])

        def recurse(bottom):
            if len(bottom) == 1:
                return True

            # helper to build the next level
            def build(i, s):
                if i == len(bottom) - 1:
                    return recurse(s)

                pair = bottom[i:i+2]
                if pair not in hs:
                    return False

                for m in hs[pair]:
                    if build(i + 1, s + m):
                        return True
                return False

            return build(0, "")

        return recurse(bottom)
