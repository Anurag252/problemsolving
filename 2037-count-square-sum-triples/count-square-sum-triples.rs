impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut res = 0;
        for i in 1..n + 1 {
            for j in 1..n + 1 {
                for k in 1..n + 1 {
                    if i * i + j * j == k * k {
                        res += 1;
                    }
                    //print!("{} {} {}\n", i*i , j*j , k*k);
                }
            }
        }
        res
    }
}