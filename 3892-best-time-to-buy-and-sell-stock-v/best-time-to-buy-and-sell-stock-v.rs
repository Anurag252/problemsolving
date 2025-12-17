impl Solution {
    pub fn maximum_profit(prices: Vec<i32>, k: i32) -> i64 {
        // we basically want to buy at i and sell at j 
        // so that i < j , so find a peak and then find smallest number before that
        // can be make more money by doing this multiple times of just at one 
        // peak => we make more money by doing this every time
        // so find all the peaks and then find the number just after the peak before it ,
        // say buy and sell or sell and buy
        // so most likely a dp
        // T[0,n,k] = max(T[i,n,k-1] + put(0,i) or short(0,i))
        // where put(0,i) mean we buy at 0 and sell at i
        // where short(0,i) mean we sell at 0 and buy at i
        // this runs n2 times 
        let n = prices.len();
        let k = k as usize;
        let mut memo = vec![vec![vec![-1; 3]; k + 1]; n];
        
        fn dfs(i: i32, j: i32, state: i32, prices: &Vec<i32>, memo: &mut Vec<Vec<Vec<i64>>>) -> i64 {
            let i_usize = i as usize;
            let j_usize = j as usize;
            let state_usize = state as usize;
            
            if j_usize == 0 {
                return 0;
            }
            if i_usize == 0 {
                return if state_usize == 0 { 0 } else if state_usize == 1 { -prices[0] as i64 } else { prices[0] as i64 };
            }
            if memo[i_usize][j_usize][state_usize] != -1 {
                return memo[i_usize][j_usize][state_usize];
            }
            
            let p = prices[i_usize] as i64;
            let res = match state {
                0 => {
                    let a = dfs(i - 1, j, 0, prices, memo);
                    let b = dfs(i - 1, j, 1, prices, memo) + p;
                    let c = dfs(i - 1, j, 2, prices, memo) - p;
                    a.max(b).max(c)
                }
                1 => {
                    let a = dfs(i - 1, j, 1, prices, memo);
                    let b = dfs(i - 1, j - 1, 0, prices, memo) - p;
                    a.max(b)
                }
                _ => {
                    let a = dfs(i - 1, j, 2, prices, memo);
                    let b = dfs(i - 1, j - 1, 0, prices, memo) + p;
                    a.max(b)
                }
            };
            memo[i_usize][j_usize][state_usize] = res;
            res
        }
        
        dfs(n as i32 - 1, k as i32, 0, &prices, &mut memo)
    }
    }
