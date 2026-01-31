impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        let mut left : i32  = 0;
        let mut right : i32= (letters.len() - 1 ) as i32;

        while(left < right) {
            let mut mid = ((left + right) / 2) as i32;
            if letters[mid as usize] <= target {
                left = mid  as i32 + 1;
            }
            else{
                right = mid;
            }
        }
        if right == letters.len() as i32 - 1 && letters[right as usize] <= target{
            return letters[0];
        }
        letters[left as usize]
    }
}