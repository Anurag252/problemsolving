use std::cmp::max;
impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let mut found = false;
        let mut res = 0;

        while(left < nums1.len() && right < nums2.len() ) {
            if found {
                if nums1[left] <= nums2[right] {
                    res = max(res, right - left);
                    right += 1;
                } else {
                    found = false;
                    
                    print!("{} {}\n", right, left);
                    left += 1
                }
            } else {
                if nums1[left] <= nums2[right] {
                    res = max(res, right - left);
                    right += 1;
                    found = true;
                    continue;
                } else {
                    left += 1;
                    right += 1;
                }
            }
            
           
        }

        

        //res = max(res, right - left - 1 ); // in one case -2
        print!("{} {}\n", right, left);
        res as i32
        
    }
}