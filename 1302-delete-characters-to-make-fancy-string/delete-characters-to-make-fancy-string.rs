use std::collections::HashMap;
impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        let mut left : usize = 0;
        let mut right : usize = 0 ;
        let mut result : String = "".to_string();
        let mut chars = HashMap::new();
        let s_chars: Vec<char> = s.chars().collect();

        while right < 2 && right < s.len() {
            chars.entry(s_chars[right]).and_modify(|x| *x += 1).or_insert(1);
            result += &(s_chars[right]).to_string();
            right += 1;
        }
 
        while right < s.len() {
            chars.entry(s_chars[right]).and_modify(|x| *x += 1).or_insert(1);
            //println!("{:?}", chars);
            if chars.len() == 1 {
                
            } else {
                result += &(s_chars[right]).to_string()
            }
            chars.entry(s_chars[left]).and_modify(|x| *x -= 1);
            if chars.get(&s_chars[left]) == Some(&0) {
                chars.remove(&s_chars[left]);
            }
            left += 1 ;
            
            right += 1;
        }
        result

    }
}