class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        hash_map={}
        for num in nums:
            hash_map[num]=1
        while True:
             if original not in hash_map:
                 return original 
             original*=2 
class TestApp:
    def test_case_one(self):
        assert Solution().findFinalValue([5,3,1,6,12],3)==24 
    def test_case_two(self):
        assert Solution().findFinalValue([2,7,9],4)==4
        
        
        
        