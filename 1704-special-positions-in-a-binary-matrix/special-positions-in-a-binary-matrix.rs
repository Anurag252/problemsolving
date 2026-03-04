use itertools::enumerate;

impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        for (i, row) in enumerate(&mat) {
            for (j, &val) in enumerate(row) {
                // Only consider cells that are 1
                if val != 1 {
                    continue;
                }

                // Check no other 1 exists in row i
                let row_ok = mat[i].iter().filter(|&&x| x == 1).count() == 1;

                // Check no other 1 exists in column j
                let col_ok = mat.iter().filter(|r| r[j] == 1).count() == 1;

                if row_ok && col_ok {
                    res += 1;
                }
            }
        }
        res
    }
}