use std::collections::HashMap;

impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        // helper for mC2
        fn fact(a: i64) -> i64 {
            (a * (a - 1)) / 2
        }

        let mut hs: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();

        // group points by y
        for k in points {
            hs.entry(k[1]).or_insert(Vec::new()).push((k[0], k[1]));
        }

        let modulo: i64 = 1_000_000_007;

        // compute fact(m) for each group
        let mut f: Vec<i64> = hs.values().map(|v| fact(v.len() as i64)).collect();

        // linear-time sum over all pairs
        let mut total: i64 = 0;
        let mut sum_f: i64 = f.iter().sum();
        for fi in f {
            sum_f -= fi;
            total = (total + fi * sum_f) % modulo;
        }

        total as i32
    }
}
