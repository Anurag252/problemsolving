class Solution:
    def __init__(self):
        self.a = {}
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        r = "".join(str(books))
        if r in self.a:
            return self.a[r]
        total = 0
        t = []
        result = 1000000
        i = 0
        for k in books:
            
            if total + k[0] <= shelfWidth:
                t.append(k[1])
                total += k[0]
                result = min(result, max(t) +  self.minHeightShelves( books[i+1:], shelfWidth))
            else:
                break
            i += 1
        #print(books, result)
        self.a[r] = 0 if result == 1000000 else result
        return self.a[r]

            


        