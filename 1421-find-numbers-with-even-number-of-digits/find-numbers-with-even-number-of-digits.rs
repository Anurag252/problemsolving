impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        for num in nums {
            let num_as_string = num.to_string();
            if num_as_string.len() % 2 == 0 {
                res += 1
            }

        }
        return res

    }
}