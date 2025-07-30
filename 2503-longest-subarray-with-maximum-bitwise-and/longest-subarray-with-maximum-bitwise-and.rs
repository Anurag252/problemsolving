
 use std::cmp::max;
 impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        /*
            maximum bitwise AND would be just one number 
            or a group of number that are same
            is it largest number ??
            I guess so 
        */
        let mut result = 0;
        let mut temp = 1;
        let mut mx = nums.iter().max();
        match mx {
            Some(min) => {
                for (i, k) in nums.iter().enumerate() {
            if k == min {
                if (i > 0 && nums[i-1] == *k) {
                    temp += 1;
                }
            } else {
                temp = 1;
            }

            result = max(result, temp);
        }
        result
            },
            None      => return 0,
        }
        

    }
}