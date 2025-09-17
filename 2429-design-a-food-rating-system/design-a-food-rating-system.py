class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mp = {}
        self.cu = {}
        for f,r, c in zip(foods, ratings, cuisines):
            self.mp[f] =(c,r)
            if c not in self.cu:
                self.cu[c] = (f, r)
            else:
                t = self.cu[c]
                if r > t[1]:
                    self.cu[c] = (f ,max(r, t[1]))
                if r == t[1]:
                    self.cu[c] = (min(f,t[0] ) ,t[1])


    def changeRating(self, food: str, newRating: int) -> None:
        self.mp[food] = (self.mp[food][0], newRating)
        cusine = self.mp[food][0]
        f,r = self.cu[cusine]
        if r > newRating and f == food: # its possible f food is being changed # then we must find a new match
            new_food, rating = "z", 0
            for k,v in self.mp.items():
                if v[0] == cusine and rating < v[1]:
                    rating = v[1]
                    new_food = k
                elif v[0] == cusine and rating == v[1]:
                    new_food = min(k, new_food)
            self.cu[cusine] = (new_food, rating)
            return

        if r < newRating:
            self.cu[cusine] = (food ,newRating)
        if r == newRating:
            self.cu[cusine] = (min(food, f) ,r)
        

    def highestRated(self, cuisine: str) -> str:
        return self.cu[cuisine][0]

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)