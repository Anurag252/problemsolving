impl Solution {
    pub fn closest_target(words: Vec<String>, target: String, start_index: i32) -> i32 {
        let n = words.len() as i32;
        let mut ans = n;
        let mut found = false;
        
        for (i, word) in words.iter().enumerate() {
            if word == &target {
                let dist = (i as i32 - start_index).abs();
                let distance = dist.min(n - dist);
                ans = ans.min(distance)
            }
        }
        
        if ans < n {
            ans
        } else {
            -1
        }
    }
}