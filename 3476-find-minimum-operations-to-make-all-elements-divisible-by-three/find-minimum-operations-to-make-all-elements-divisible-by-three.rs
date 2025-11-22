impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut res = 0;

        for k in nums {
            if (k % 3 == 2) {
                res += 1;
            } else {
                res += (k % 3);
            }
            
        }
        res
    }
}