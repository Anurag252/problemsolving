impl Solution {
    pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
        // sort and pair largest with smallest 
        // is it possible that there is larger ?
        // [1,5,5,5] -> yes 
        // take all sum then

        let mut arr = nums.clone();
        arr.sort();
        let mut res = 0;
        for  i in 0..arr.len()-1 {
            if arr[i] + arr[arr.len()-1 - i]  > res {
                res = arr[i] + arr[arr.len() - 1 - i] ;
            }
        }
        res
    }
}