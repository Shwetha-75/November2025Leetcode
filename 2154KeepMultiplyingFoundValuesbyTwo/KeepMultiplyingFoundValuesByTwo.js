/**
 * @param {number[]} nums
 * @param {number} original
 * @return {number}
 */
var findFinalValue = function(nums, original) {
    let hash_map={};
    for(let num in nums){
        hash_map[num]=1
    }

    while(true){
        if(!original.toString() in hash_map){
            return original;
        }
        original*=2

    }
};