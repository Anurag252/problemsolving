impl Solution {
    pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
        // 2n elements , but n + 1 unique elements
        // one element occurs half the time
        // majority voting algo
        // if the elements occurs half the time 
        // then only in one condition two elements will not occur togather
        // a x a y z a
        // in rest all cases we can find two consecutive elements
        // if we do not find consecutive element then first or last element must be an ans
        // so loop again
        let mut prev = -1;
        for k in nums.clone() {
            if prev == k {
                return k;
            } else {
                prev = k;
            }
        }

        let mut first = nums[0];
        let mut res = 0;
        for k in nums.clone() {
            if first == k {
                res += 1;
            }
        }

        if res > 1 {
            return first;
        }


        let mut last = nums[nums.len() - 1];
        let mut res = 0;
        for k in nums.clone() {
            if last == k {
                res += 1;
            }
        }

        if res > 1 {
            return last;
        }
        last
    }
}