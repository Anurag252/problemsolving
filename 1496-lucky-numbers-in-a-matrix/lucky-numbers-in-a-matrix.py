class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result =[]
        d = set()
        for k in matrix:
            d.add(min(k))
        elem = 0
        for l in range(len(matrix[0])):
            elem = 0
            for k in range(len(matrix)):
                elem = max(matrix[k][l], elem)
            if elem in d:
                result.append(elem)
        return result


            

        