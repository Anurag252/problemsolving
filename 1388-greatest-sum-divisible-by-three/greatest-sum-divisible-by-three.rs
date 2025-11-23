use std::cmp::max;

impl Solution {
    pub fn max_sum_div_three(mut nums: Vec<i32>) -> i32 {
        // add all
        // remove the 2 1s
        // remove 1 2s
        // remove 1s
        let mut s = 0;
        let mut one : Vec<i32> = Vec::new();
        let mut two : Vec<i32> = Vec::new();
        nums.sort();
        for k in nums {
            s += k;
            if k % 3 == 1 {
                one.push(k)
            }


            if k % 3 == 2 {
                two.push(k)
            }
        }
        //print!("{} {} {}", one1, two1, two2);
        if s % 3 == 0 {
            return s;
        }
        //print!("{} {} {}", one1, two1, two2);
        if s % 3 == 1 {

            if one.len() > 0 && two.len() > 1 {
                return max(s - one[0] , s - two[0] - two[1]);
            } else if one.len() > 0 {
                return s - one[0];
            } else if two.len() > 1 {
                return s - two[0] - two[1]
            } else {
                return 0;
            }
           
        }

        //print!("{} {} {} {}", one1, two1, two2, s);
        if s % 3 == 2 {

            if two.len() > 0 && one.len() > 1 {
                return max(s - two[0] , s - one[0] - one[1]);
            } else if two.len() > 0 {
                return s - two[0];
            } else if one.len() > 1 {
                return s - one[0] - one[1]
            } else {
                return 0;
            }
        }

        return 0;
    }
}