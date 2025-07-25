use std::collections::HashSet;
use libc::abs;

impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
       // it appears to be maximum subsequence of 
       // given array with unique numbers and max sum
       // idea is take all largest unique +ve numbers 
       // order does not matter
        let mut nums_hash = HashSet::new();
       let mut res = 0;
       let mut has_positive = false;
       let mut vec_cloned : Vec<i32> = nums.clone();
       vec_cloned.sort_by(|a, b| b.cmp(a));
       for k in vec_cloned {
        if nums_hash.contains(&k) {
            continue;
        }
        nums_hash.insert(k);
        if k > 0 {
            res += k;
            has_positive = true
        } else {
            if (! has_positive) {
                return k;
            }

        }
        
       }
       res
    }
}