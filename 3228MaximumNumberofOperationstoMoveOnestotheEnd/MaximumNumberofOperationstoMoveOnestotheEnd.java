class MaximumNumberofOperationstoMoveOnestotheEnd{
    private class Solution{
      public int maxOperations(String s) {
         int n=s.length(),startIndex=n-1,impact=1,ans=0,count_ones=0;
         for(int i=0;i<n;i++){
            if(s.charAt(i)=='1'){
                  count_ones++;
            }
         }
         if(count_ones==n) return 0;
         for(int i=n-1;i>-1;i--){
            if(s.charAt(i)=='0'){
                startIndex=i;
                break;

            }
         }
         int i=startIndex;
         while(i>=0){
            if(s.charAt(i)=='0'){
                i--;
                continue;
            }
            int j=i,count=0;
            while(j>-1){
                if(s.charAt(j)=='1'){
                    count++;

                }else{
                    break;
                }
                j--;
            }
            ans+=count*impact;
            impact++;
            i=j-1;
         }

        return ans;

       }
    }
}