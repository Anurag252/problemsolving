use std::cmp::max;

impl Solution {
    pub fn area_of_max_diagonal(dimensions: Vec<Vec<i32>>) -> i32 {
        let mut area = 0;
        let mut diag = 0;
        let mut prev = 0;

        for k in dimensions.clone() {
            diag = max(k[0].pow(2) + k[1].pow(2), diag);
        }

        for k in dimensions {
            if diag == k[0].pow(2) + k[1].pow(2) {
                area = max(area, k[0] * k[1]);
            }
        }

        return area;
    }
}