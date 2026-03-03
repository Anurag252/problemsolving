impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        
        fn test(a : &str, n : i32) -> String {
            if n == 0 {
                return a.to_string();
            }
            let mut b = a.chars().rev().collect::<String>();
            let mut c = String::new();
            for z in b.chars() {
                if z == '1' {
                    c.push('0');
                } else {
                    c.push('1');
                }
            }

            return test(&(a.to_owned() + "1" + &c), n - 1);

        }
        let mut g = "0";
        return test(g, n).chars().nth((k - 1) as usize).unwrap();
    }
}