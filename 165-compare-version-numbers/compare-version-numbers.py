class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
            split by dot, then append smaller one with 0
            parse each 01 as 1

        """
        v1 = version1.split(".")
        v2 = version2.split(".")

        if len(v1) < len(v2):
            for _ in range(0, len(v2)- len(v1)):
                v1.append(0)
        else:
            for _ in range(0, len(v1)- len(v2)):
                v2.append(0)
        print(v1, v2)
        for (k,l) in zip(v1, v2):
            if int(k) < int(l):
                return -1
            if int(k) > int(l):
                return 1
        return 0

