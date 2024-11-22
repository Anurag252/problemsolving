class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # let's say there is a row that is good, flipping it will make it bad
        # two rows become good after flips if rows are equal or complimentary
        # find rows that have same values and complimentatry values are same.
        # take max of both 
        arr = {}
        coml_arr = {}

        for row in matrix:
            key = ",".join(list(map(str,row)))
            if key in arr:
                arr[key] += 1
            else :
                arr[key] = 1

            compl_row = list(map(lambda x : "1" if x == 0 else "0", row))
            compl_key = ",".join(compl_row)
            if compl_key in arr:
                arr[compl_key] += 1
            else:
                arr[compl_key] = 1
        
        ans = 0
        #print(arr)
        for k1 in arr.values():
            ans = max(ans, k1)

        return ans



        