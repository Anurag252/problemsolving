public class Solution {
    public void SolveSudoku(char[][] board) {
        Calc(board);
    }
    
  public bool  Calc(char[][] board)
    {
        for(int i = 0 ; i < 9 ; i ++)
        {
           for(int j = 0 ; j < 9 ; j ++)
            {
                if(board[i][j] == '.')
                {
                    var ls = findValidList(board , i , j);
                    if(ls.Count > 0)
                    {
                        foreach(var item in ls)
                        {
                            board[i][j] = item.ToString()[0];

                            if(Calc(board))
                            {
                                return true ;
                            }

                        }
                        board[i][j] = '.';
                        return false;
                        //findValidList(board , i , j)
                        
                        
                    }
                    else
                    {
                        return false;
                    }
                    
                }
            } 
        }
      return true;
    }


public List<int> findValidList(char[][] board , int i , int j)
{
    int[] arr = new int[9];
    for(int k = 0 ; k < 9 ; k ++)
    {
        if(board[k][j] != '.')
        {
            arr[Int32.Parse(board[k][j].ToString()) - 1] = 1;
        }
        
        if(board[i][k] != '.')
        {
            //Console.WriteLine(Int32.Parse(board[i][k].ToString()) - 1);
            arr[Int32.Parse(board[i][k].ToString()) - 1] = 1;
        }
                
    }
    
     int k1 = 3*(i / 3) + 2;
         int l = 3*(j / 3) + 2;

         for (int c = 3 * (i / 3); c <= k1; c++)
         {
             for (int x = 3 * (j / 3); x <= l; x++)
             {
                 if (board[c][x] != '.')
                 {
                     arr[Int32.Parse(board[c][x].ToString()) - 1] = 1;
                 }
             }

         }
    
    
    List<int> ls = new List<int>();
    for(int k = 0 ; k < 9 ; k ++)
    {
        if(arr[k] == 0)
        {
            ls.Add(k + 1);
        }
        
    }
    return ls;
}
}