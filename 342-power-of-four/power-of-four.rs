impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
       // bin of 2 is 10, 100 is 4, 1000 is 8, 10000 is 16
       let mut k = (n as f32).log2();
       if (k as i32) as f32 != k.ceil() {
        return false;
       }
       return k as i32 % 2 == 0;
    }
}