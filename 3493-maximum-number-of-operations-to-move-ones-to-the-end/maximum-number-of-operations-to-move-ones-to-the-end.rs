use itertools::enumerate;
impl Solution {
    pub fn max_operations(s: String) -> i32 {
        // max operations would mean that 
        // move the 1s from the left first 
        // maybe count the 1s separated by 0 ?
        // 1100011100010110100
        // 2,3,1,2,1
        // here result would be 2 + (2 + 3) + (2 + 3+ 1) ...
        // k * (len - i)
        let mut arr = Vec::new();
        let mut temp :i32 = 0;
        for k in s.chars() {
            if k == '1' {
                temp += 1;
            } else {
                if temp > 0 {
                    arr.push(temp);
                    temp = 0;
                }
                
            }
            
        }

        //print!("{:?}", arr);
        let mut res = 0;
        for (i,k) in enumerate(arr.clone()) {
            res += (k * (arr.len() - i) as i32);
        }
        res
    }
}