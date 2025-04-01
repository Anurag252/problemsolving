class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] = max points starting from i

        for i in range(n - 1, -1, -1):
            points, skip = questions[i]
            take = points + (dp[i + skip + 1] if i + skip + 1 < n else 0)
            skip = dp[i + 1]
            dp[i] = max(take, skip)

        return dp[0]
