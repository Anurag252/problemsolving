impl Solution {
    pub fn sum_zero(n: i32) -> Vec<i32> {
        let mut arr = Vec::new();

        for  i in -(n/2)..=(n/2) {
            if i == 0 {
                if 2*arr.len() == n as usize {
                    continue;
                }
            }
             arr.push(i);
        }
        arr
    }
}