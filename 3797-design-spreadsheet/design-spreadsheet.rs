struct Spreadsheet {
    arr : Vec<Vec<i32>>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Spreadsheet {

    fn new(rows: i32) -> Self {
        let mut arr : Vec<Vec<i32>> = Vec::new();
        for i in 0..rows {
            let mut tmp : Vec<i32> = Vec::new();
            for j in 0..26 {
                tmp.push(0);
            }
            arr.push(tmp);
        }
        let mut spreadSheet = Spreadsheet{
            arr : arr
        };
        return spreadSheet

    }
    
    fn set_cell(&mut self, cell: String, value: i32) {
    // parse as Excel style: Letter = column, Number = 1-based row
    let mut chars = cell.chars();
    let col_char = chars.next().unwrap().to_ascii_lowercase();
    let row_str: String = chars.collect();
    let row: usize = row_str.parse::<usize>().unwrap() - 1;
    let col = (col_char as u8 - b'a') as usize;

    self.arr[row][col] = value;
}

fn reset_cell(&mut self, cell: String) {
    // same parsing as set_cell
    let mut chars = cell.chars();
    let col_char = chars.next().unwrap().to_ascii_lowercase();
    let row_str: String = chars.collect();
    let row: usize = row_str.parse::<usize>().unwrap() - 1;
    let col = (col_char as u8 - b'a') as usize;

    self.arr[row][col] = 0;
}

    
    fn get_value(&self, formula: String) -> i32 {
    let args = formula.replace("=", "");
    let str_arr = args.split('+');
    let mut result = 0;

    for k in str_arr {
        println!("{:?}", k);

        if let Some(first) = k.chars().next() {
            if first.is_ascii_alphabetic() {
                // ✅ Only treat as cell if first char is a letter
                let mut chars = k.chars();
                let first = chars.next().unwrap().to_ascii_lowercase();
                let col_str: String = chars.collect();
                let row: usize = col_str.parse().unwrap();

                println!("{:?} --- {:?}", first, row);

                if ('a'..='z').contains(&first) {
                    let col = (first as u8 - b'a') as usize;
                    result += self.arr[row - 1][col]; // rows are 1-indexed
                }
                continue;
            }
        }

        // otherwise parse as number
        if let Ok(num) = k.parse::<i32>() {
            result += num;
        }
    }

    result
}

}


/**
 * Your Spreadsheet object will be instantiated and called as such:
 * let obj = Spreadsheet::new(rows);
 * obj.set_cell(cell, value);
 * obj.reset_cell(cell);
 * let ret_3: i32 = obj.get_value(formula);
 */