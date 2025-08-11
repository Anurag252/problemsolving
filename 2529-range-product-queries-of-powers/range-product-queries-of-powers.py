class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        def recurse(n, res):
            if n == 0:
                return True
            if n < 0:
                return False
            b = n.bit_length() - 1
            for k in range(b, -1, -1):
                if recurse(n - 2**k, res):
                    res.append(2**k)
                    return True
            return False

    
        a = []
        recurse(n, a)

        # build prefix products modulo MOD
        prefix = []
        m = 1
        for k in a:
            m = (m * k) % MOD
            prefix.append(m)

        results = []
        for l, r in queries:
            if l == 0:
                val = prefix[r]
            else:
                # modular inverse needed here for correct mod division
                # but since Python big int, let's do modular inverse with pow
                val = prefix[r] * pow(prefix[l-1], MOD-2, MOD) % MOD
            results.append(val)

        return results
