impl Solution {
    pub fn maximum69_number (num: i32) -> i32 {
        // maybe change first 6 to 9
        let mut a = 0;
        for (i,k) in (num.to_string()).chars().enumerate() {
            if k == '6' {
                a = i;
                break;
            }
        }
        let mut owned_string: String = "".to_owned();
        owned_string.push_str(&(num.to_string())[..a]);
        owned_string.push_str("9");
        owned_string.push_str(&(num.to_string())[a+1..]);
        return (owned_string).parse::<i32>().unwrap();

    }
}