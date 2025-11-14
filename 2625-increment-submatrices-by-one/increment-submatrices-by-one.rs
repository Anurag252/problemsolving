impl Solution {
    pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        // brute forcing will TLE
        // if we make the array as single dim array as its only 500
        // then convert the rows to single dim
        // then add 1 at start and -1 after end 
        //n = 3 
        // 0,1,2,3,4,5,6,7,8
        // 0,0 -> 0
        // 0,1 -> 1
        // 0,2 -> 2
        // 1,0 -> 3 = row * col_max + col
        // 1,1 -> 3
        // given this is square , this addressing may not work
        // the thing is I need to somehow mark the submatrix 
        // GAVE UP, BUT THINK MORE ON ABOVE APPORACH, this was correct

        let n = n as usize;
        let mut diff = vec![vec![0; n+1]; n+1];
        for q in queries.iter() {
            let (row1, col1, row2, col2) = (q[0] as usize, q[1] as usize, q[2] as usize, q[3] as usize);
            diff[row1][col1] += 1;
            diff[row2+1][col1] -= 1;
            diff[row1][col2+1] -= 1;
            diff[row2+1][col2+1] += 1;
        }

        let mut mat = vec![vec![0; n]; n];
        for i in 0..n {
            for j in 0..n {
                let x1 = if i == 0 { 0 } else { mat[i-1][j] };
                let x2 = if j == 0 { 0 } else { mat[i][j-1] };
                let x3 = if i == 0 || j == 0 { 0 } else { mat[i-1][j-1] };
                mat[i][j] = diff[i][j] + x1 + x2 - x3;
            }
        }
        mat
    }
}