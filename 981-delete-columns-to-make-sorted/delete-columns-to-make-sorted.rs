 use itertools::enumerate;

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let mut arr : Vec<Vec<char>> = Vec::new();

        

        for k in strs {

            for (i, m) in enumerate(k.chars()) {
                if (arr.len()) <= i {
                    print!("here");
                    arr.push(Vec::new());
                }
                arr[i].push(m);
            }
        }
        let mut a = 0;
        for mut m in arr {
            let u = m.clone();
            m.sort();
            if u != m {
                a += 1;
            }
        }
        a

    }
}