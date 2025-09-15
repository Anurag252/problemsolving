use std::collections::HashSet;
impl Solution {
    pub fn can_be_typed_words(text: String, broken_letters: String) -> i32 {
        let mut res = 0;
        let mut hs = HashSet::new();

        for b in broken_letters.chars() {
            hs.insert(b);
        }

        for k in text.split(" "){
            let mut found = false;
            for m in k.chars() {
                if hs.contains(&m) {
                    found = true;
                    break;
                }
            }
            if !found{
                res += 1;
            }
        }
        return res;
    }
}