use std::collections::HashMap;

impl Solution {
    pub fn max_distance(colors: Vec<i32>) -> i32 {
        let mut memo = HashMap::new();
        Self::solve(&colors, 0, colors.len() - 1, &mut memo)
    }

    fn solve(colors: &[i32], start: usize, end: usize, memo: &mut HashMap<(usize, usize), i32>) -> i32 {
        if start >= end {
            return 0;
        }
        if let Some(&res) = memo.get(&(start, end)) {
            return res;
        }

        let res = if colors[start] != colors[end] {
            (end - start) as i32
        } else {
            let left = Self::solve(colors, start + 1, end, memo);
            let right = Self::solve(colors, start, end - 1, memo);
            std::cmp::max(left, right)
        };
        memo.insert((start, end), res);
        res
    }
}