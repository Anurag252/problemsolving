use std::collections::HashSet;

impl Solution {
    pub fn number_of_pairs(points: Vec<Vec<i32>>) -> i32 {
        // upper left is x <= mx and y >= my
        // to form a rect - mx and nx and my and ny , no points should lie here
        // n is 50, so we could just nest two loops
        // to find if a point lies in rect, we need to keep sorted arr of both x and y and find common between both arrays
        // that's third loop -> we could also perform bin search here 
        // 
        let mut x_sorted = points.clone();
        x_sorted.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut y_sorted = points.clone();
        y_sorted.sort_by(|a, b| a[1].cmp(&b[1]));
        let mut res = 0;
        for k in &points {
            for l in &points {
                if k == l {
                    continue
                }
                let ax = k[0];
                let ay = k[1];
                let bx = l[0];
                let by = l[1];
                
                if ax > bx || ay < by {
                    continue;
                }

                let mut valid = true;
                for m in &points {
                    if m == k || m == l {
                        continue;
                    }
                    if ax <= m[0] && m[0] <= bx && by <= m[1] && m[1] <= ay {
                        valid = false; // point lies inside or on boundary
                        break;
                    }
                }

                if valid {
                    res += 1;
                }

            }
        }
        res
    }
}