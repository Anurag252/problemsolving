/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    int sum = 0 ;
    public int SumRootToLeaf(TreeNode root) {
        string s = "";
        Calc(root ,s);
        return sum ;
    }
    
    public void Calc(TreeNode root , string s)
    {       
        if(root == null)
        {
            return ;
        }
        if( root.left == null && root.right == null)
        {
            
            Console.WriteLine(s);
            sum = sum + Convert.ToInt32(s + root.val , 2);
            return ;
        }
        Calc(root.left , s + root.val);
        
        Calc(root.right , s + root.val);
    }
}