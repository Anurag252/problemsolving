impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, capacity: Vec<i32>) -> i32 {
        let mut c = capacity.clone();
        c.sort_by(|a,b| b.cmp(a));
        let mut total : i32 = apple.into_iter().sum();
        let mut res = 0;
        for k in c.clone() {
            total -= k;
            res += 1;
            if total <= 0 {
                return res;
            }
        }
        return res;
    }
}