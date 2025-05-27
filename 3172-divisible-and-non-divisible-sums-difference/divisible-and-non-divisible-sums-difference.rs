impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        let mut sum1 = 0;
        let mut sum2 = 0;
        for  i in  1..=n {
            if i % m == 0 {
                sum1 += i;
            }
            sum2 += i;
        }
        return sum2 - 2*sum1;
    }
}