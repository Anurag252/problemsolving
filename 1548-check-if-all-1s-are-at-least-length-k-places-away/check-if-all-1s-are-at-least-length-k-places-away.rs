impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut diff = -1;

        for m in nums {
            if diff == -1 && m == 0 {
                continue;
            }

            if diff == -1 && m == 1 {
                diff = 0;
                continue;
            }

            if m == 0 {
                
                diff += 1;
            } else {
                if diff < k {
                    
                    return false;
                } else {
                    diff = 0;
                }
            }
        }
        return true;
    }
}