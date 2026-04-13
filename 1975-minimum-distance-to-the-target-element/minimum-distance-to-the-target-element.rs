use itertools::enumerate;
impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        
        let mut res = 100000;
        for (i, k) in enumerate(nums.clone()) {
            if k == target {
                if (i as i32-start).abs() < res {
                    res = (i as i32-start).abs();
                }
            }
            
        }
        res
    }
}