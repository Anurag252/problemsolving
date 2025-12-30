use std::collections::HashSet;
impl Solution {
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        


        fn is_magic_square(g: Vec<Vec<i32>>) -> bool {
            //print!("{:?}", g);
            let mut a = 0;
            for k in g.clone() {
                let mut s = 0;
                for m in k {
                    s += m
                }
                if a == 0 {
                    a = s
                } else {
                    if (a != s) {
                        return false
                    }
                }
            }

            if a != g[0][0] + g[1][1] + g[2][2] {
                return false;
            }

            if a != g[0][2] + g[1][1] + g[2][0] {
                return false;
            }

            if a != g[0][0] + g[1][0] + g[2][0] {
                return false;
            }

            if a != g[0][1] + g[1][1] + g[2][1] {
                return false;
            }

            if a != g[0][2] + g[1][2] + g[2][2] {
                return false;
            }

            let mut hs = HashSet::new();
            hs.insert(g[0][0]);
            hs.insert(g[0][1]);
            hs.insert(g[0][2]);
            hs.insert(g[1][0]);
            hs.insert(g[1][1]);
            hs.insert(g[1][2]);
            hs.insert(g[2][0]);
            hs.insert(g[2][1]);
            hs.insert(g[2][2]);
            if hs.len() != 9 {
                return false;
            }
            if hs.contains(&0) {
                return false;
            }
            if g[0][0] + g[0][1] + g[0][2] + g[1][0] + g[1][1] + g[1][2] + g[2][0] + g[2][1] + g[2][2]  != 45 {
                return false;
            }
            return true;
        }


        let mut i  = 0;
        let mut j = 0;
        let mut ans = 0;
        for i in 0..grid.len() {
            
            let mut d = i;
            for j in 0..grid[i].len() {
                let mut m = Vec::new();
                
                while(d < i + 3) {
                    let mut n = Vec::new();
                    if j + 2 < grid[i].len() && d < grid.len() {
                    n.push(grid[d][j]);
                    n.push(grid[d][j+1]);
                    n.push(grid[d][j+2]);
                    } else {
                        break
                    }
                    d += 1;
                    m.push(n.clone());
                    //print!("{:?} nnnnn", m);
                }
                
                if m.len() == 3 && is_magic_square(m.clone()) {
                    ans += 1;
                }


                d = i;
                
            }
        }

        return ans;
        
    }
}