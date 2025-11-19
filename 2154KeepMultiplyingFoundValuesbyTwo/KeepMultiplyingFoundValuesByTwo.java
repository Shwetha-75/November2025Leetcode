import java.util.LinkedHashMap;

class KeepMultiplyingFoundValuesByTwo {
      private class Solution{
        public int findFinalValue(int[] nums, int original) {
           LinkedHashMap<Integer,Integer> map=new LinkedHashMap<Integer,Integer>();
          for(int num:nums){
            map.put(num,1);
          }
          while(true){
            if(!map.containsKey(original)){
              return original;
            }
            original*=2;
          }

        }
      }
}
