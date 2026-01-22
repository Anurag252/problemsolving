impl Solution {
    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        let mut temp = nums.clone();
        let mut res = 0;

        fn is_not_non_decreasing(t: &[i32]) -> bool {
            for i in 1..t.len() {
                if t[i - 1] > t[i] {
                    return true;
                }
            }
            false
        }

        while is_not_non_decreasing(&temp) {
            let mut best_sum = i32::MAX;
            let mut indx = 0;

            for i in 0..temp.len() - 1 {
                let s = temp[i] + temp[i + 1];
                if s < best_sum {
                    best_sum = s;
                    indx = i;
                }
            }

            temp.splice(indx..=indx + 1, [best_sum]);
            res += 1;
        }

        res
    }
}
