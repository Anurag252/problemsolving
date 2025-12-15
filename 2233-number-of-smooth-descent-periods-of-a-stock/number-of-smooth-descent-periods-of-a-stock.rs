use itertools::enumerate;
impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        // we probably need continuos sequences wh9ch decreases
        // then if size is n  do 1 + 2 + .. (n-1)
        // also add all single ones
        let mut temp = 1;
        let mut res = Vec::new();
        let mut l = prices.len();
        for (i, k) in enumerate(prices.clone()) {
            if i == 0 {
                res.push(temp);
                temp = 1;
                continue;
            }
            if k + 1 == prices[i-1] {
                temp += 1;
            } else {
                res.push(temp);
                temp = 1;
            }
        }

        res.push(temp);
        let mut ans = 0;

        for k in res {
            ans += (k * (k-1)) / 2
        }
        ans + l as i64


    }
}