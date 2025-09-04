impl Solution {
    pub fn find_closest(x: i32, y: i32, z: i32) -> i32 {
        if (z - x).abs() > (z-y).abs() {
            return 2;
        } else if (z - x).abs() == (z-y).abs() {
            return 0;
        } else {
            return 1 ;
        }
    }
}