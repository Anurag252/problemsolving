class Solution:
    def predictTheWinner(self, nums: List[int], sum_a : int = 0, sum_b : int = 0 , is_a_turn : bool = True ) -> bool:
        print(nums, sum_a, sum_b, is_a_turn)
        if len(nums) == 0:
            if is_a_turn:
                return sum_a >= sum_b
            else:
                return sum_a < sum_b

        if is_a_turn:
            if self.predictTheWinner(nums[:-1], sum_a + nums[len(nums)-1] , sum_b, not is_a_turn ) == False:
                return True
            if self.predictTheWinner(nums[1:], sum_a + nums[0] , sum_b, not is_a_turn ) == False:
                return True
            return False
        else :
            if self.predictTheWinner(nums[:-1], sum_a  , sum_b + nums[len(nums)-1], not is_a_turn ) == False:
                return True
            
            if self.predictTheWinner(nums[1:], sum_a  , sum_b + nums[0], not is_a_turn ) == False :
                return True
            return False
            

        