// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn balance_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        // how abt i just take amiddle 
        // element and then 
        // find mid of left and right
        // and create left and right 
        let mut arr : Vec<i32> = Vec::new();

        fn recurse(root: Option<Rc<RefCell<TreeNode>>>, arr: &mut Vec<i32>) {
    if let Some(node) = root {          // “If the file exists…”
        let node_ref = node.borrow();   // “Open the file for reading”
        recurse(node_ref.left.clone(), arr);  // “Read left child”
        arr.push(node_ref.val);                // “Read this file’s value and save it”
        recurse(node_ref.right.clone(), arr); // “Read right child”
    }
}

        recurse(root, &mut arr);
        
        fn build(arr: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if arr.is_empty() { return None; }
            let mid = arr.len() / 2;
            let root = Rc::new(RefCell::new(TreeNode::new(arr[mid])));
            root.borrow_mut().left = build(&arr[..mid]);
            root.borrow_mut().right = build(&arr[mid+1..]);
            Some(root)
        }

        
        //print!("{:?}", arr);
        return build(&arr);
    }
}