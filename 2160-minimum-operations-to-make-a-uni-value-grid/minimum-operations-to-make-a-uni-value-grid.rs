use std::cmp::min;
use std::collections::HashSet;
impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {

        /* its always apossible ? No ,shortest path is just  step behind
        many destinations ?
        maybe mmost frequent element is an unique number
        one of the number from array is unique number
        grid is not relevant ? it could be an array ?
        could binary search be possible ?
        we search for ans ?
        sum(arr) + knx // m is an integer ?

        m0st promising is choose each number from gid
        then find the diff between then
        [2,4,6,8] -> [4,4,4,4] 16-12 = 4 which means 2x
        [2,0,2,2*2] // not this does not work as plus 2 and -2 are eaten by each other and we never find ans
        given that 10000 is the limit of 
        choose 1 to 10K
        for each select and element as answer and perform the op on array ?
        */
        let mut hs = HashSet::new();
        let mut a = 0;
        let mut new_arr = Vec::new();

        
         for arr in grid.clone(){
                for j in arr {
                    new_arr.push(j);
                    a = j;
                    hs.insert(a);
                }
         }

         if new_arr.len() == 1 {
            return 0;
         }

         new_arr.sort();
         let dest = new_arr[new_arr.len() / 2];
         
        let mut res = 10000000;
        let mut temp = 0;
        let mut invalid = false;
        for j in new_arr.clone(){
                        //print!("{} {} {}\n", k as i32,j,x);
            if ((dest - j) % x != 0) {
                temp = 10000000;
                break;
            }
            temp += ((dest - j) / x).abs();
                       
        }
        res = temp;
                //print!("{}\n", temp as i32);
        if res == 10000000 {
            return -1;
        }
        return res;
        
    }
}