impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut res : Vec<Vec<i32>> = Vec::new();
        let mut temp : Vec<i32> = Vec::new();
        temp.push(1);
        res.push(temp.clone());
        for i in 1..num_rows {
            let mut f = 0;
            let mut r = 1;
            let mut temp_to_add = Vec::new();
            temp_to_add.push(1);
            while (r < temp.len()) {
                temp_to_add.push(temp[f] + temp[r]);
                f += 1;
                r += 1;
            }
            temp_to_add.push(1);
            res.push(temp_to_add.clone());
            temp = temp_to_add;
        }
        res
    }
}