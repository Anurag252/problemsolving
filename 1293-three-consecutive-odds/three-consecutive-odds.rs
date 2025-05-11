impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        let mut count = 0;
        for k in arr {
            if k % 2 != 0 {
                count += 1;
            } else {
                count = 0;
            }

            if count == 3 {
                return true;
            }
        }

        return false;
    }
}