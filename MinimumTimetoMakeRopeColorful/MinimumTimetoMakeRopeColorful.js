/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    let stack=[[colors[0],neededTime[0]]],n=colors.length,max_value=0;
    for(let i=0;i<n;i++){
        if(stack[stack.length-1][0]==colors[i]){
            if(stack[stack.length-1][1]<neededTime[i]){
                let temp=stack.pop();
                max_value+=temp[1]
                stack.push([colors[i],neededTime[i]])
            }else{
                max_value+=neededTime[i]
            }
        }else{
            stack.push([colors[i],neededTime[i]])
        }
    }
    return max_value
};