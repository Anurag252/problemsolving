use std::collections::HashMap ;
use std::cmp::max;

impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        let mut mp = HashMap::new();
        for k in dominoes {
            if k[0] > k[1] {
                let state = mp.entry((k[1], k[0])).or_insert(0);
                *state += 1;

            } else {
                let state = mp.entry((k[0], k[1])).or_insert(0);
                *state += 1;
            }
            
        }
        let mut res = 0;
        for (k,v) in mp {
            if v > 1 {
                res += v * (v-1) / 2;
            }
        }
        return res 
    }
}