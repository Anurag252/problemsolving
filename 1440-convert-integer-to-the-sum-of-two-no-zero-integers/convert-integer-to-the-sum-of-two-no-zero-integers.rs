impl Solution {
    pub fn get_no_zero_integers(n: i32) -> Vec<i32> {
        for i in 1..=n {
            let mut a = i;
            let mut matched = true;
            while( a >= 10) {
                
                if a % 10 == 0 {
                    matched = false;
                    break;
                }
                a = a / 10;
            }
            if !matched {
                continue;
            }
            a = n - i;
            while( a >= 10) {
                
                if a % 10 == 0 {
                    matched = false;
                    break;
                }
                a = a / 10;
            }
            if matched {
                return [i, n-i].to_vec();
            }
        }
        return [0,0].to_vec();
    }
}