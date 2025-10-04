public class Solution {
    public int MaxArea(int[] nums) {
        
        int end = nums.Length-1 ;
        
        int max_area = 0 ;
        
        for(int i = 0 ; i < nums.Length ; i ++)
        {
            
            if(nums[i] <= nums[end])
            {
                max_area = Math.Max(max_area , (end - i ) * nums[i] );
            }
            else
            {
                int j = end ;
                
                while(nums[j] <= nums[i] && j > i)
                {
                    max_area = Math.Max(max_area , (j - i )*nums[j] );
                    j = j -1 ;
                }
                max_area = Math.Max(max_area , (j - i )*nums[i] );
            }
        }
        return max_area ;
            
    }
}