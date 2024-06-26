public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        SortedList<char , int> dict = new SortedList<char , int>();
        
        for(int i = 0 ; i < tasks.Length ; i ++)
        {
            if(dict.ContainsKey(tasks[i]))
            {
                dict[tasks[i]] = dict[tasks[i]] + 1;
            }
            else
            {
                dict.Add(tasks[i] , 1);
            }
        }
        
        var t  = dict.OrderByDescending(x => x.Value);
        
        int availableSpace = (t.First().Value-1)*n;
        Console.WriteLine(availableSpace);
        Console.WriteLine(t.First().Value);
        for(int i = 1 ; i < t.Count() ; i++)
        {
            
            Console.WriteLine(t.ElementAt(i).Value);
            
            //in case frequency is same as maximum
            availableSpace = availableSpace - Math.Min( t.First().Value-1 ,t.ElementAt(i).Value);
            //Console.WriteLine(availableSpace);
        }
        //what to do if  availableSpace is negative
        availableSpace = Math.Max(availableSpace , 0);
        
        return availableSpace + tasks.Length;
        
        
    }
}