class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n=len(nums)
        g=num1=0
        for num in nums:
            if num==1:
               num1+=1
            g=self.gcd(num,g)
        if g>1:return -1
        if num1>0:
            return n-num1
             
        # find gcd exist or not 
        min_len=n
        for i in range(n):
            g=0
            for j in range(i,n):
                g=self.gcd(g,nums[j])
                if g==1:
                    min_len=min(min_len,j-i+1)
                    break
        return min_len+n-2
    def gcd(self,a:int,b:int):
        if a==0 or b==0:
            return a if not b else b
        res=min(a,b)
        while res>0:
            if a%res==0 and b%res==0:
                break 
            res-=1
        return res
class TestApp:
    def test_case_one(self):
        assert Solution().minOperations([2,6,3,4])==4
    def test_case_two(self):
        assert Solution().minOperations([2,10,6,14])==-1
    def test_case_three(self):
        assert Solution().minOperations([6,10,15])==4
    def test_case_four(self):
        assert Solution().minOperations([1,3,4,5,1])==3
            