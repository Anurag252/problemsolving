impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n == 2 || n == 1 {
             return true
        }
        if n % 2 != 0 || n == 0 {
            return false;
        }
        return Self::is_power_of_two(n/2)
    }
}