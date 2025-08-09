impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        use std::collections::HashMap;

        let mut memo: HashMap<(i32, i32), (f64, f64)> = HashMap::new();

        pub fn recurse(a: i32, b: i32, memo: &mut HashMap<(i32, i32), (f64, f64)>) -> (f64, f64) {
            if a <= 0 && b <= 0 {
                return (0.0, 1.0);
            }
            if a <= 0 {
                return (1.0, 0.0);
            }
            if b <= 0 {
                return (0.0, 0.0);
            }

            if let Some(&res) = memo.get(&(a, b)) {
                return res;
            }

            let (pa1, pb1) = recurse(a - 100, b, memo);
            let (pa2, pb2) = recurse(a - 75, b - 25, memo);
            let (pa3, pb3) = recurse(a - 50, b - 50, memo);
            let (pa4, pb4) = recurse(a - 25, b - 75, memo);

            let res = (
                (pa1 + pa2 + pa3 + pa4) / 4.0,
                (pb1 + pb2 + pb3 + pb4) / 4.0,
            );

            memo.insert((a, b), res);
            res
        }

        if n > 4800 {
            return 1.0;
        }

        let (pa, pb) = recurse(n, n, &mut memo);
        pa + 0.5 * pb
    }
}
