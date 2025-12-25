impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, mut k: i32) -> i64 {
        // if i just sort the arr
        // just keep picking the largest and reduce temp
        // k times 
        happiness.sort_by(|a,b| b.cmp(a));
        let mut temp  = 0;
        let mut res : i64 = 0;
        for m in happiness {
            
            if m - temp <= 0 || k == 0 {
                //print!("{} {} ab", res, temp);
                return res;
            }
            res += (m - temp) as i64;
            temp += 1;
            k -= 1;
            //print!("{} {}", res, temp);
        }
        //print!("{} {} cd", res, temp);
        return res;
    }
}