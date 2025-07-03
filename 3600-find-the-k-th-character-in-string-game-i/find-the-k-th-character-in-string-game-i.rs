impl Solution {
    pub fn kth_character(k: i32) -> char {
        let mut arr : [char; 5001]= ['a'; 5001];
        let mut curr = 1;
        while(curr < k) {
            let sl: Vec<char> = arr[0..curr as usize].to_vec();
            let mut i  = 0;
            for m in sl.iter() {
                if (*m  == 'z') {
                    arr[curr as usize+i] = 'a';
                } else {
                    arr[curr as usize+i] = ((*m as u8) + 1) as char;
                }
                i += 1
                
            }
            curr *= 2      
        }
        //println!("{:?}",&arr[0..=curr as usize]);
        return arr[(k - 1) as usize]

    }
}