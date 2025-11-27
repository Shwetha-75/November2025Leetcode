class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        max_total,n=float('-inf'),len(nums)
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                if (j-i+1)%k==0:
                    max_total=max(max_total,sum)
        print(max_total)
        return max_total
import sys
class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n=len(nums)
        min_so_far=[sys.maxsize//2]*k 
        min_so_far[k-1]=0 
        prefix_sum,max_sum=0,float('-inf')
        for i in range(n):
            prefix_sum+=nums[i]
            max_sum=max(max_sum,prefix_sum-min_so_far[i%k])
            min_so_far[i%k]=min(min_so_far[i%k],prefix_sum)
        return max_sum
      
class TestApp:
    def test_case_one(self):
        assert Solution().maxSubarraySum([1,2],1)==3
    def test_case_two(self):
        assert Solution().maxSubarraySum([-1,-2,-3,-4,-5],4)==-10
    def test_case_three(self):
        assert Solution().maxSubarraySum([-5,1,2,-3,4],2)==4