impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        // START BY PLACING THE largest fruit 
        // if largest fruit is placed in a so can all other fruits be placed
        // no it says leftmost basket
        // in that case simply assign to each basket
        // one way is 2 for loop
        // what if we keep a track of largest basket to the left
        let mut result = 0;
        let mut baskets_mut = baskets.clone();
        for k in fruits {
            let mut found = false;
            for l in baskets_mut.iter_mut() {
                if k <= *l {
                    *l = 0;
                    found = true;
                    break;
                }
            }
            if ! found {
                result += 1;
            }
        }
        return result;


    }
}