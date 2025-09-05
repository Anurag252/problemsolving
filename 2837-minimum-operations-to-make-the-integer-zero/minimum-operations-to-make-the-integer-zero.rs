use std::cmp;
use std::collections::HashMap;

impl Solution {
    pub fn make_the_integer_zero(num1: i32, num2: i32) -> i32 {
        // at every step we have 61 options 
        // we have overlapping subproblems and can cache
        // T[num1] = min(T[num1 - 2i - num2]) for every i in 0 to 60
        // T[0] = 1
        // if num1 < num2 -> prune, find once n then anything > n prune
        // is it greedy 
        // bottom up is larger than top down or DFS 
        // if num1 = 2i + 2j + 2k + num2*l // 
        // so the diff is 2i + 2j + 2k + num2(l-1) -> a multiple of num2 and a binary number
        // so the answer can always be reached , for minimum steps
        // find how many 1s are there in remaining and is it equal to l-1
        // use 2^0 + 2^2 + 2^7 -> 7 bits
        // num2(l-1) l-1 values
        // if we say these are not minimum,
        // have a feeling but no proof that this must always be converging
        // 
        let mut k  = 1;
        while true {
            let diff: i64 = num1 as i64 - num2 as i64 * k as i64;


            if diff < k {
                return -1;
            }
            let mut a :i64 = diff;
            let mut count = 0;
            while(a > 0) {
                if a & 1 == 1 {
                    count += 1;
                }
                a = a >> 1;
                
            }

            if count <= k {
                return k as i32;
            }
            k += 1;



        }

        return -1
        
    }
}