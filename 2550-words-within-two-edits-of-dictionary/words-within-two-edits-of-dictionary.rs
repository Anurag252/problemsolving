impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        let mut ans = Vec::new();

        for query in &queries {
            for s in &dictionary {
                let mut dis = 0;
                for (c1, c2) in query.chars().zip(s.chars()) {
                    if c1 != c2 {
                        dis += 1;
                    }
                }
                if dis <= 2 {
                    ans.push(query.clone());
                    break;
                }
            }
        }

        ans
    }
}