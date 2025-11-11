use std::cmp::max;
use std::collections::HashMap;

impl Solution {
    pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
        // loop and count
        // ambiguos problem 
        // so we need to find subset that is global
        // larger subset would mean smaller strings
        // sort by size and take the strs
        // as there are two constraints
        // it may not be simple to just pick one of two
        // pick one and recurse for rest or do not pick one and recurse
        fn recurse(strs : &Vec<String>, i : i32, m : i32, n :i32, memo: &mut HashMap<(i32, i32, i32), i32>) -> i32 {
            if i == strs.len() as i32 {
                return 0; // after last elem return 0
            }
            if m < 0 || n < 0 {
                return -1000; // leads to smaller set 
            }
            if memo.contains_key(&(i,m,n)) {
                return memo[&(i,m,n)];
            }
            let mut zeros = 0;
            let mut ones = 0;
            for c in strs[i as usize].chars() {
                if c == '1' {
                    ones += 1;
                } else {
                    zeros += 1;
                }
            }
            if m - zeros < 0 || n - ones < 0 {
                return recurse(strs, i + 1, m , n, memo);
            }
            let mut a = 1 + recurse(strs, i + 1, m - zeros, n - ones, memo );
            let mut b = recurse(strs, i + 1, m , n, memo);
            memo.insert((i,m,n), max(a,b));
            return max(a,b);

        }
        let mut memo : HashMap<(i32, i32, i32), i32> = HashMap::new();
        recurse(&strs, 0, m, n, &mut memo)
    }
}