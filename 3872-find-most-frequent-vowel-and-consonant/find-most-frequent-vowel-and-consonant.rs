use std::collections::HashMap;
use std::cmp::max;
impl Solution {
    pub fn max_freq_sum(s: String) -> i32 {
        
        let mut vowel = HashMap::new();
        let mut consonant = HashMap::new();

        for  k in s.chars() {
            if k == 'a' || k == 'e' || k == 'i' || k == 'o' || k == 'u' {
                match vowel.get(&k) {
                    Some(count) => vowel.insert((k.clone()), count + 1),
                    None => vowel.insert((k.clone()), 1)
                };
            } else {
                match consonant.get(&k) {
                    Some(count) => consonant.insert(k.clone(), count + 1),
                    None => consonant.insert(k.clone(), 1)
                };
            }
        }
        let mut a = 0;
        let mut b = 0;
        for (k, v) in vowel {
            a = max(v, a);
        }

        for (k, v) in consonant {
            b = max(v, b);
        }

        return a + b
    }
}