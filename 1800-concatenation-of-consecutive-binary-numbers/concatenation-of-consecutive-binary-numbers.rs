impl Solution {
    pub fn concatenated_binary(n: i32) -> i32 {
        let mut result: i64 = 0;
        let modulo: i64 = 1_000_000_007;
        let mut bit_length = 0;

        for i in 1..=n {
            // If i is power of 2, increase bit length
            if (i & (i - 1)) == 0 {
                bit_length += 1;
            }

            result = ((result << bit_length) + i as i64) % modulo;
        }

        result as i32
    }
}