/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubPath(head *ListNode, root *TreeNode) bool {
    
    if (root == nil) {
        return head == nil
    }

    if head == nil {
        return true
    }



    if head.Val == root.Val {
        if (check(head.Next, root.Left) || check(head.Next, root.Right)) {
            return true
        }
    }

    return  isSubPath(head, root.Left) || isSubPath(head, root.Right)
}

func check(head *ListNode, root *TreeNode) bool {
    if (root == nil) {
        return head == nil
    }

    if head == nil {
        return true
    }
     if head.Val == root.Val {
        if (check(head.Next, root.Left) || check(head.Next, root.Right)) {
            return true
        }
    }
    return false
}