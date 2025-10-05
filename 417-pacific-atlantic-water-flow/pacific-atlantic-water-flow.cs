public class Solution {
    public IList<IList<int>> PacificAtlantic(int[][] matrix) {
     
         int n = matrix.Length;
        
         if(n == 0)
        {
            IList<IList<int>> lsa = new List<IList<int>>();
                  
            return lsa;
        }
        
         int m = matrix[0].Length;
         IList<IList<int>> ls = new List<IList<int>>();
        bool[,] pacific = new bool[matrix.Length ,matrix[0].Length];
        bool[,] atlantic = new bool[matrix.Length ,matrix[0].Length];
        int[,] visited = new int[matrix.Length ,matrix[0].Length];
        
              
        
         for(int i = 0 ; i < n ; i++)
        {         
            for(int j = 0 ; j < m ; j++)
            {
                if(i == 0 || j == 0)
                {
                  pacific[i,j] = true;
                }
                
                if(i == n-1 || j == m-1)
                {
                    atlantic[i,j] = true;
                }
            }
             
         }
        
        for(int i = 1 ; i < n ; i++)
        {         
            for(int j = 1 ; j < m ; j++)
            {
               if(visited[i,j] == 0)
               {
                   Calc(matrix , visited , pacific , i , j);
                  
               }
            }
            
        }
         visited = new int[matrix.Length ,matrix[0].Length];
        
         
        
         for(int i = n-1 ; i >= 0 ; i--)
        {         
            for(int j = m-1 ; j >= 0 ; j--)
            {
               if(visited[i,j] == 0)
               {
                   Calc(matrix , visited , atlantic , i , j);
                  
               }
            }
            
        }
        
         for(int i = 0 ; i < n ; i++)
        {         
            for(int j = 0 ; j < m ; j++)
            {
                if(pacific[i,j] == true && atlantic[i,j] == true)
                {
                    List<int> ls1 = new List<int>();
                    ls1.Add(i);
                    ls1.Add(j);
                    ls.Add(ls1);
                }
            }
             
         }
        
        
        return ls;
        
    }
        
         
        public bool Calc(int[][] matrix , int[,] visited , bool[,] ocean , int i , int j)
        {
           
            
            
            if(ocean[i,j])
            {
                return true;
            }
            
           
            
            
            if(i+1 < matrix.Length && visited[i+1,j] == 0)
            {
                   
                if(matrix[i+1][j] <= matrix[i][j])
                { visited[i,j] = 1;
                
                    bool t = Calc(matrix , visited , ocean , i +1 , j);
                    if(t)
                    {
                        
                         visited[i,j] = 0;
                        ocean[i,j] = true;
                       
                        return true;;
                    }
                    visited[i,j] = 0;
                }
            }
            
            
            if(j+1 < matrix[0].Length && visited[i,j+1] == 0)
            {
                   
                if(matrix[i][j+1] <= matrix[i][j])
                { visited[i,j] = 1;
                
                    bool t = Calc(matrix , visited , ocean , i  , j+1);
                    if(t)
                    {
                        visited[i,j] = 0;
                       
                        ocean[i,j] = true;
                        return true;
                    }
                    visited[i,j] = 0;
                }
            }
            
            
            if(i-1 >= 0 && visited[i-1,j] == 0)
            {
                    
                if(matrix[i-1][j] <= matrix[i][j])
                {
                    visited[i,j] = 1;
                 
                    bool t = Calc(matrix , visited , ocean , i -1 , j);
                    if(t)
                    {
                        visited[i,j] = 0;
                      
                        ocean[i,j] = true;
                        return true;
                    }
                    visited[i,j] = 0;
                }
            }
            
            
            
            if(j-1 >= 0 && visited[i,j-1] == 0)
            {
                   
                if(matrix[i][j-1] <= matrix[i][j])
                {
                     visited[i,j] = 1;
                  
                    bool t = Calc(matrix , visited , ocean , i  , j-1);
                    if(t)
                    {
                        visited[i,j] = 0;
                      
                        ocean[i,j] = true;
                        return true;
                    }
                    visited[i,j] = 0;
                }
            }
            
            
            return false;
            
        }
        
    
}
    