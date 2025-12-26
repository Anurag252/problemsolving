use std::iter::zip;
use itertools::enumerate;

impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let n = customers.len();
        let chars: Vec<char> = customers.chars().collect();

        // N[i] = number of 'N' before i
        let mut N = vec![0; n + 1];
        for i in 0..n {
            N[i + 1] = N[i] + if chars[i] == 'N' { 1 } else { 0 };
        }

        // Y[i] = number of 'Y' after i
        let mut Y = vec![0; n + 1];
        for i in (0..n).rev() {
            Y[i] = Y[i + 1] + if chars[i] == 'Y' { 1 } else { 0 };
        }

        let mut res = i32::MAX;
        let mut ans = 0;

        for (i, (y, n_)) in enumerate(zip(Y.iter(), N.iter())) {
            let penalty = y + n_;
            if penalty < res {
                res = penalty;
                ans = i;
            }
        }

        ans as i32
    }
}
