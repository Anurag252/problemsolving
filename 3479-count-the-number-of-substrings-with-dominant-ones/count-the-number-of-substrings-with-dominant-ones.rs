impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        // some kind of sliding window
        // when you find 1, then count all 1s
        // all 1s (with 0 0s) + (all 1s starting from first 1 with 0 0s - 1)+ 
        //all 1s starting from first 1 with 0 0s, with 1 0s, 

        //101101
        //10,11,21,31,32,42 -> 
        //
        //4 + 1 + 
        // no this does not work
        // n2 is easy
        // for sliding windw we need to find when should we keep inc
        // its not possible right ? 
        // maybe try to find the non-dominant
        // if you see a 0 then 
        // maybe prefix sum works
        // 101101
        // 10,11,21,31,32,42 -> 1 and 0s
        // let's analyze first what would it take to count equal numbers of 1s and 0s
        // we add 1 for each 1 and reduce 1 for each 1
        // then two indexes having same number have equale number of 1s and 0s
        // GAVE UP
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut pre = vec![-1; n + 1];
        for i in 0..n {
            if i == 0 || chars[i - 1] == '0' {
                pre[i + 1] = i as i32;
            } else {
                pre[i + 1] = pre[i];
            }
        }

        let mut res = 0i32;
        for i in 1..=n {
            let mut cnt0 = if chars[i - 1] == '0' { 1 } else { 0 };
            let mut j = i as i32;
            while j > 0 && (cnt0 * cnt0) as usize <= n {
                let cnt1 = (i as i32 - pre[j as usize]) - cnt0;
                if cnt0 * cnt0 <= cnt1 {
                    res += std::cmp::min(j - pre[j as usize], cnt1 - cnt0 * cnt0 + 1);
                }
                j = pre[j as usize];
                cnt0 += 1;
            }
        }
        res
    }
}
