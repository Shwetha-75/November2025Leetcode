class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        val n: Int = colors.length
        var max_value: Int = 0
        var stack: MutableList<MutableList<Int>> =mutableListOf(mutableListOf(colors.get(0).code, neededTime[0]));
        for(i in 1..<n){
            val new_item=mutableListOf(colors.get(i).code,neededTime.get(i));
            val old_item=stack.get(stack.size-1);
            if(old_item.get(0)==colors.get(i).code){
                
               if(old_item.get(1)<neededTime.get(i)) {

                   max_value+=old_item.get(1);
                   stack.removeAt(stack.size-1);
                   stack.add(new_item);
                }
                else{
                    max_value+=neededTime.get(i);
    
                }

            }else{
                stack.add(new_item);
            }
        }

        return max_value;   

    }
}
