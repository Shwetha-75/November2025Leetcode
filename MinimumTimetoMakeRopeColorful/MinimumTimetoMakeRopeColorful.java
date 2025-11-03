
import java.util.LinkedList;
import java.util.List;

public class MinimumTimetoMakeRopeColorful {

    private class Solution{
    public int minCost(String colors, int[] neededTime) {
        int max_value=0,n=colors.length();
        List<List<Integer>> stack=new LinkedList<>();
        List<Integer> list= new LinkedList<>();
        list.add((int)colors.charAt(0));
        list.add(neededTime[0]);
        stack.add(list);
        for(int i=1;i<n;i++){
            List<Integer> new_item=new LinkedList<>();
            new_item.add((int)colors.charAt(i));
            new_item.add(neededTime[i]);    
            List<Integer> last_item=stack.get(stack.size()-1);
            if(last_item.get(0)==(int)colors.charAt(i)){
                 if(last_item.get(1)<neededTime[i]){
                    max_value+=last_item.get(1);
                    stack.remove(stack.size()-1);
                    stack.add(new_item);
                 }else{
                    max_value+=neededTime[i];
                 }

            }else{
                stack.add(new_item);
            }
        }
        return max_value;
    }
    }
}