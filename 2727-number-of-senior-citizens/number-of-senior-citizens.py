class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for k in details:
            if int(k[11:13]) > 60:
                result += 1
        return result

        