impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        let mut found_zeros = false;

        for k in s.chars() {
            if k.to_digit(10).unwrap() == 0 {
                found_zeros = true;
            }

            if k.to_digit(10).unwrap() == 1 && found_zeros {
                return false;
            }
        }
        return true;

    }
}