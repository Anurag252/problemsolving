impl Solution {
    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        
        // Precompute trailing zeros for each row
        let mut trailing_zeros: Vec<usize> = vec![0; n];
        for i in 0..n {
            let mut count = 0;
            for j in (0..n).rev() {
                if grid[i][j] == 0 {
                    count += 1;
                } else {
                    break;
                }
            }
            trailing_zeros[i] = count;
        }
        
        // Row i needs at least (n - 1 - i) trailing zeros
        let mut swaps = 0;
        let mut rows = trailing_zeros.clone();
        
        for i in 0..n {
            let needed = n - 1 - i;
            
            // Find the closest row at or below i that satisfies the requirement
            let mut found = None;
            for j in i..n {
                if rows[j] >= needed {
                    found = Some(j);
                    break;
                }
            }
            
            match found {
                None => return -1,
                Some(j) => {
                    // Bubble row j up to position i
                    swaps += (j - i) as i32;
                    // Shift rows down
                    for k in (i+1..=j).rev() {
                        rows.swap(k, k-1);
                    }
                }
            }
        }
        
        swaps
    }
}
