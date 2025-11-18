impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        

        fn recurse(i : i32, arr : Vec<i32>) -> bool {
            //print!("{}", i);
            if i == arr.len()  as i32 - 1{
                return true;
            }

            if i > arr.len()  as i32 - 1{
                return false;
            }

            if i == arr.len() as i32 - 2 && arr[i as usize] == 1 {
                return false;
            }

            if arr[i as usize] == 0 {
                return recurse(i + 1, arr);
            } else {
                // this was 1 and that means 10 or 11
                return recurse(i + 2, arr);
            }
            

        }

        return recurse(0, bits);
    }
}