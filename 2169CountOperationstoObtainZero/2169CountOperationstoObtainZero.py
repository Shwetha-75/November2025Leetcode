class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count=0
        while num1 and num2:
            if num1>=num2:
                num1-=num2 
            else:
                num2-=num1 
            count+=1
        return count 
class TestApp:
    def test_case_one(self):
        assert Solution().countOperations(2,3)==3
    def test_case_two(self):
        assert Solution().countOperations(10,10)==1
            