impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        // if R and L is same , U an dD is same
        let mut total_h = 0;
        let mut total_v = 0;
        for k in moves.chars() {
            if k == 'L' {
                total_h += 1
            }

            if k == 'R' {
                total_h -= 1
            }


            if k == 'U' {
                total_v += 1
            }

            if k == 'D' {
                total_v -= 1
            }

        }

        if total_h == 0 && total_v == 0 {
            return true;
        }
        return false;
    }
}