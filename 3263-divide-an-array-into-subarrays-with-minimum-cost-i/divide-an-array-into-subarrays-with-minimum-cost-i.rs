impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i32 {
        let mut a = 100000;
        let mut b = 100000;

        for k in &nums[1..] {
            if *k < a {
                b = a;
                a = *k;
            } else if *k < b {
                b = *k;
            }
        }

        return nums[0] + a + b;
    }
}