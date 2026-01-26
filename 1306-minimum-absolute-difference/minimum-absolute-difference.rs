 use std::collections::HashMap;
 use itertools::enumerate;

impl Solution {
    pub fn minimum_abs_difference(arr: Vec<i32>) -> Vec<Vec<i32>> {
        let mut hs: HashMap<i32, Vec<Vec<i32>>> = HashMap::new();
        let mut s = arr.clone();

        s.sort();

        for i in 1..s.len() {
            let diff = s[i] - s[i - 1];

            if !hs.contains_key(&diff) {
                hs.insert(diff, Vec::new());
            }

            let z = vec![s[i - 1], s[i]];
            hs.get_mut(&diff).unwrap().push(z);
        }

        let mut g = i32::MAX;
        let mut res = Vec::new();

        for (a, b) in hs {
            if a < g {
                g = a;
                res = b;
            }
        }

        res
    }
}