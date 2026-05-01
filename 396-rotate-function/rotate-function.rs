use itertools::enumerate;
use std::cmp::max;
impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        //10 10 1 2 3 4
        //1 2 3 4 10/10
        // the idea i can think of is to have a 2 d multiplication  table of numbers and index
        // and look up the numbers -> no does not work
        // the idea is that I will have to calculate this product one way or the other
        // without calcualtion I cannot think of a way
        // since numbers varies from -100 to 100 
        // I can calculate the product like 
        // for each index * an arrya of 200 numbers ( pprefiiled with contents of array)
        // and store it
        // after that create a 2D array and store it there
        // so index 0 fills the table for all elements of array bu looping only 
        // 200 times
        // then sum rows to find the max.
        /*I could add at the time of building the table. 
        another approach is I calculate sum once then difference with rotated arr sum can be predicted ? 
        if k is at 0 and k is at 1. the difference is sum of all elements from 1 to end - first * k, 
        maybe there is a pattern ? yeah there is convoluted sum - sum + k*elem -> can be calculated in one go
        */
        let mut con_sum = 0;
        let mut sum = 0;
        let nums_cloned = nums.clone();
        let mut res = 0;
        let mut prefix_sum = Vec::new();
        let mut suffix_sum = Vec::new();


        for (i, k) in enumerate(nums_cloned) {
            con_sum += (k * i as i32);
            sum += k;
        }

        res = con_sum;

        let mut temp = 0;

        for k in nums.clone() {
            suffix_sum.push(sum-temp);
            temp += k;
            prefix_sum.push(temp);
            

        }

        //print!("{:?} {:?}", prefix_sum, suffix_sum);
        let mut new_sum = 0;
        for (i, k) in enumerate(nums.clone()) {
            if i == 0 {
                continue;
            }
            //print!("{} {}", con_sum, res);
            res = max(res, con_sum - sum + (nums.len()  as i32 ) * nums[i-1]   );
            con_sum = con_sum - sum + (nums.len()  as i32 ) * nums[i-1]   ;
            //print!("{} {}\n", con_sum, res);
        }

        res


    }
}