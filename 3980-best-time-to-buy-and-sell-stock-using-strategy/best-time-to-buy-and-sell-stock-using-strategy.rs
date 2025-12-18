impl Solution {
    pub fn max_profit(prices: Vec<i32>, strategy: Vec<i32>, k: i32) -> i64 {
        // maintain two arrs, prefix and suffix on original prices
        // and prefix and suff on strategy * prices
        // slide window of k , between i and j indexes
        // deduct strategy * prices sum from total  between i and j 
        // add prices (consider 1 as strategy) from i + k/2 to j and find new  total
        // find max of thiese 
        let n = prices.len();
        let mut profit_sum = vec![0i64; n + 1];
        let mut price_sum = vec![0i64; n + 1];
        for i in 0..n {
            profit_sum[i + 1] = profit_sum[i] + prices[i] as i64 * strategy[i] as i64;
            price_sum[i + 1] = price_sum[i] + prices[i] as i64;
        }
        let mut res = profit_sum[n];
        for i in (k - 1) as usize..n {
            let left_profit = profit_sum[i - (k as usize) + 1];
            let right_profit = profit_sum[n] - profit_sum[i + 1];
            let change_profit = price_sum[i + 1] - price_sum[i - (k as usize) / 2 + 1];
            res = res.max(left_profit + change_profit + right_profit);
        }
        res
    }
}