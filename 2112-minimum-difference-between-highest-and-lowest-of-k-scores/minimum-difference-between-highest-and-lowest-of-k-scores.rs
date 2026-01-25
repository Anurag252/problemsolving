impl Solution {
    pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
        if k <= 1 || k as usize > nums.len() {
            return 0;
        }

        let mut arr = nums.clone();
        arr.sort();

        let k = k as usize;
        let mut m = k - 1;
        let mut diff = i32::MAX;

        while m < arr.len() {
            diff = diff.min(arr[m] - arr[m - k + 1]);
            m += 1;
        }

        diff
    }
}
