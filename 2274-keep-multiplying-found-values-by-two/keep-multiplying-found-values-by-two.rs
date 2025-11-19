use std::collections::HashMap;
impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        let mut hs = HashMap::new();

        for k in nums {
            if !hs.contains_key(&k) {
                hs.insert(k,k);
            }
        }
        let mut orig = original;
        while (orig != -1) {
            if hs.contains_key(&orig) {
                orig = orig * 2;
            } else {
                return orig;
                orig = -1;
            }
        }
        return -1;

    }
}