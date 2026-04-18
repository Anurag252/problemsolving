impl Solution {
    pub fn mirror_distance(n: i32) -> i32 {
        let mut s = n.to_string();
        s = s.chars().rev().collect();
        let mut a = s.parse::<i32>().unwrap();
        (a - n).abs()
    }
}