impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {

        if n == 1 {
            return true;
        }
        if n < 1 {
            return false;
        }
        if n % 3 != 0 {
            return false;
        }
        return Self::is_power_of_three(n / 3)
    }
}