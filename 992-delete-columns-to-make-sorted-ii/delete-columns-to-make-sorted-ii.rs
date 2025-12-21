use std::collections::HashSet;

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        print!("{:?}", strs);
        let mut hs: HashSet<usize> = HashSet::new();

        for (i, k) in strs.iter().enumerate() {
            for l in strs[i..].iter() {
                if k > l {
                    for (x, (m, n)) in k.chars().zip(l.chars()).enumerate() {
                    
                    if m > n {
                        // we must skip the index
                        hs.insert(x);
                        break;
                    }
                }
                }
                
                if hs.len() > 0 {
                    break;
                }
            }
            if hs.len() > 0 {
                break;
            }
        }

        if hs.len() == 0 {
                return 0;
            }

        let mut new_arr = Vec::new();

        for m in strs.clone() {
            let mut a = Vec::new();
            for (i,l) in m.chars().enumerate() {
                if hs.contains(&i){
                    continue;
                }
                a.push(l);
            }
            new_arr.push(a.into_iter().collect());
        }

        return 1 + Self::min_deletion_size(new_arr);

        hs.len() as i32
    }
}
