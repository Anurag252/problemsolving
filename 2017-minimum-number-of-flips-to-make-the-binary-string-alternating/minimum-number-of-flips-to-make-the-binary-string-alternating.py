class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s  # All rotations appear as substrings

        # Build target patterns
        a = "".join("1" if i % 2 == 0 else "0" for i in range(2 * n))
        b = "".join("0" if i % 2 == 0 else "1" for i in range(2 * n))

        # Count mismatches in the initial window [0, n)
        diff_a = sum(t[i] != a[i] for i in range(n))
        diff_b = sum(t[i] != b[i] for i in range(n))

        res = min(diff_a, diff_b)

        # Slide the window across all rotations
        for i in range(n):
            # Add character entering the window (at i + n)
            diff_a += t[i + n] != a[i + n]
            diff_b += t[i + n] != b[i + n]

            # Remove character leaving the window (at i)
            diff_a -= t[i] != a[i]
            diff_b -= t[i] != b[i]

            res = min(res, diff_a, diff_b)

        return res