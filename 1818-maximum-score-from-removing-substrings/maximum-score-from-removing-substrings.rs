impl Solution {
    pub fn maximum_gain(s: String, x: i32, y: i32) -> i32 {
        let mut points = 0;
        let mut chars: Vec<char> = s.chars().collect();

        if x > y {
            points += Self::remove_all(&mut chars, 'a', 'b', x);
            points += Self::remove_all(&mut chars, 'b', 'a', y);
        } else {
            points += Self::remove_all(&mut chars, 'b', 'a', y);
            points += Self::remove_all(&mut chars, 'a', 'b', x);
        }

        points
    }

    fn remove_all(chars: &mut Vec<char>, first: char, second: char, score: i32) -> i32 {
        let mut stack = Vec::new();
        let mut points = 0;

        for &ch in chars.iter() {
            if let Some(&last) = stack.last() {
                if last == first && ch == second {
                    stack.pop();
                    points += score;
                    continue;
                }
            }
            stack.push(ch);
        }

        // Replace original vec with remaining characters for next removal round
        chars.clear();
        chars.extend(stack);
        points
    }
}
