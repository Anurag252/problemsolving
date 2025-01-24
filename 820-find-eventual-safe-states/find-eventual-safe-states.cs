public class Solution {
    HashSet<int> black = new HashSet<int>();    
    HashSet<int> dangerNode = new HashSet<int>();
    public IList<int> EventualSafeNodes(int[][] graph) {
       
        List<int> result = new List<int>();
        
        for(int i = 0; i < graph.Length ; i ++)
        {
            if(dangerNode.Contains(i))
            {
                continue;
            }
            if(black.Contains(i))
            {
                result.Add(i);
                continue;
            }
            HashSet<int> hs = new HashSet<int>();
            //Console.WriteLine();
            bool hasnoCycle = DFS(graph, i, hs);
            
            if(hasnoCycle)
            {
                result.Add(i);
            }
        }
        
        return result;
        
        
    }
    
    public bool DFS(int[][] dt, int source, HashSet<int> grey)
    {
        //Console.WriteLine(source);
        if( (dt[source].Length == 0) )
        {
            black.Add(source);
            return true;
        }
        
        
        if(black.Contains(source))
        {
            return true;
        }
        
        if(grey.Contains(source))
        {
            dangerNode.Add(source);
            //black.Add(source);
            return false;
        }
        
        grey.Add(source);
        
        for(int i = 0 ; i < dt[source].Length ; i ++)
        {
            
            
            bool hascycle = DFS(dt,dt[source][i], grey);
            if(!hascycle)
            {       
                dangerNode.Add(source);
                //black.Add(source);
                return false;                
            }
            else
            {
                //black.Add(source);
                grey.Remove(dt[source][i]);
            }
        }
          
        black.Add(source);
        return true;
    }
    
   
}