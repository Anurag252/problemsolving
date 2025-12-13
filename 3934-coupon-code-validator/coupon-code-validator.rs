use std::iter::zip;
use std::cmp::Ordering;

impl Solution {
    pub fn validate_coupons(
        code: Vec<String>,
        business_line: Vec<String>,
        is_active: Vec<bool>,
    ) -> Vec<String> {

        fn s(a: &(String, String, bool), b: &(String, String, bool)) -> Ordering {
    let arr = ["electronics", "grocery", "pharmacy", "restaurant"];

    let m = arr.iter().position(|x| x == &a.1).unwrap_or(arr.len());
    let n = arr.iter().position(|x| x == &b.1).unwrap_or(arr.len());

    if m == n {
        return a.0.cmp(&b.0);
    }
    m.cmp(&n)
}


        let mut comb_arr: Vec<(String, String, bool)> = Vec::new();

        // build combined array
        for ((k1, k2), k3) in zip(zip(code, business_line), is_active) {
            comb_arr.push((k1, k2, k3));
        }

        // keep sorting
        comb_arr.sort_by(s);

        let mut res = Vec::new();
        let allowed = ["electronics", "grocery", "pharmacy", "restaurant"];

        // add checks here
        for k in comb_arr {
            // active check
            if !k.2 {
                continue;
            }

            // business line check
            if !allowed.contains(&k.1.as_str()) {
                continue;
            }

            // code non-empty & valid chars
            if k.0.is_empty() {
                continue;
            }

            if !k.0.chars().all(|c| c.is_ascii_alphanumeric() || c == '_') {
                continue;
            }

            res.push(k.0);
        }

        res
    }
}
