impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n > 4800 {
            return 1.0;
        }
        use std::collections::HashMap;

        let mut memo: HashMap<(i32, i32), (f64, f64, f64)> = HashMap::new();

        pub fn recurse(
            a: i32,
            b: i32,
            k: f64,
            memo: &mut HashMap<(i32, i32), (f64, f64, f64)>
        ) -> (f64, f64, f64) {
            let p = f64::powf(0.25, k);

            // Return weighted result if in memo
            if let Some(&(ua, ub, uc)) = memo.get(&(a, b)) {
                return (ua * p, ub * p, uc * p);
            }

            if a <= 0 {
                if b <= 0 {
                    return (p * 0.0, p * 1.0, p * 1.0);
                } else {
                    return (p * 1.0, p * 0.0, p * 1.0);
                }
            }

            if b <= 0 {
                return (p * 0.0, p * 0.0, p * 1.0);
            }

            // Compute unweighted
            let a1 = recurse(a - 100, b, k + 1.0, memo);
            let a2 = recurse(a - 75, b - 25, k + 1.0, memo);
            let a3 = recurse(a - 50, b - 50, k + 1.0, memo);
            let a4 = recurse(a - 25, b - 75, k + 1.0, memo);

            let unweighted = (
                (a1.0 + a2.0 + a3.0 + a4.0) / p,
                (a1.1 + a2.1 + a3.1 + a4.1) / p,
                (a1.2 + a2.2 + a3.2 + a4.2) / p,
            );

            memo.insert((a, b), unweighted);
            (unweighted.0 * p, unweighted.1 * p, unweighted.2 * p)
        }

        let (a, b, c) = recurse(n, n, 0.0, &mut memo);
        a / c + 0.5 * (b / c)
    }
}
