class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n=digit_count=1
        if k%2==0 or k%5==0:
            return -1 
        rem=1
        while rem%k!=0:
            n=rem*10+1
            rem=n%k 
            digit_count+=1
        return digit_count
class TestApp:
    def test_case_one(self):
        assert Solution().smallestRepunitDivByK(1)==1
    def test_case_two(self):
        assert Solution().smallestRepunitDivByK(2)==-1
    def test_case_three(self):
        assert Solution().smallestRepunitDivByK(3)==3