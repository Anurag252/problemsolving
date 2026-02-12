use std::collections::HashMap;
impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        // only 1000 as length
        //all substrings in 10^ 6
        let mut res = 0;
        for (i,k1) in s.chars().enumerate() {
            let mut hs: HashMap<char, i32> = HashMap::new();
            for (j,k2) in s[i..].chars().enumerate() {
               *hs.entry(k2).or_insert(0) += 1;
            
            let mut a = 0;
            let mut found = true;
            for &count in hs.values() {
                if a == 0 {
                    a = count;
                } else if a != count {
                    found = false;
                    break;
                }
            }
            if found {
                res = res.max(j+ 1 );
            }
        }
        }

        return res as i32;
    }
}