class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # find the min val the sequence can take at any moment
        # also find the max val the sequ can take at any momemt
        # use prefix arr to do that
        # now lower_seq + min <= lower
        # and upper_seq + max <= upper 
        # meaning lower - min to upper - max is the seq

        mn, mx = 1000000, -1000000
        t = 0
        for k in differences:
            t += k
            mx = max(t, mx)
            mn = min(t, mn)
        print(mx, mn)
        t1 = min(upper - mx, upper)
        t2 = max(lower - mn, lower)

        return t1 - t2 + 1 if t1 - t2 + 1> 0 else 0
