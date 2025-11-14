/**
 * @param {string} s
 * @return {number}
 */
var maxOperations = function(s) {
    let n=s.length, startIndex=n-1,impact=1,count_ones=0,ans=0;
    for(let i=0;i<n;i++){
        if(s[i]==='1') count_ones++;
    }
    if(count_ones==n) return 0;
    for(let i=n-1;i>-1;i--){
        if(s[i]==='0'){
            startIndex=i;
            break;
        }
    }
    let i=startIndex;
    while(i>=0){
        if(s[i]==='0'){
            i--;
            continue;
        }
        let count=0,j=i;
        while(j>-1){
            if(s[j]==='1'){
                j--;
                count++;
            }else{

            break;
            }
        }
        ans+=impact*count;
        impact++;
        i=j-1;

    }

    return ans

};