impl Solution {
    pub fn min_operations(s: String) -> i32 {
        /*
        let mut prev = -1;
        let mut res = 0;
        for k in s.chars() {
            if prev == -1 {
                prev = k as i32;
            } else {
                if prev == k as i32{
                    res += 1;
                    if prev == 0 {
                        prev = 1;
                    } else {
                        prev = 0;
                    }
                } else {
                    prev = k as i32;
                }
            }
        }
        res*/

        // greedy failed, too fast


        // recursion of all will be too slow
        /* fn recurse(s : String) {
            let mut prev = -1;
            let mut res = 0;
            for (i,k) in enumerate(s.chars()) {
                if prev == -1 {
                    prev = k
                } else {
                    if prev == k {
                        res = 1 + recurse()
                    } else {
                        prev = k;
                    }
                }
            }
        */
        // how abt enumeration ?
        // only two possible ans, why not find the smaller diff between two srings 
        let mut res1 = 0;
        let mut res2 = 0;
        let mut init1 = 0;

        let mut init2 = 1;

        for k in s.chars() {
            //print!("{}", k.to_digit(10));
            if k.to_digit(10).unwrap() != init1 {
                res1 += 1;
            }
            
            if k.to_digit(10).unwrap() != init2 {
                res2 += 1;
            }

            if init1 == 1 {
                init1 = 0;
            } else {
                init1 = 1;
            }


            if init2 == 1 {
                init2 = 0;
            } else {
                init2 = 1;
            }

        }
        print!("{} {}", res1, res2);
        return res1.min(res2);

    }
}