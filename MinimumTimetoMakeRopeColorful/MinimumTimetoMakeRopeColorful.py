class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        max_value,n=0,len(colors)
        stack=[[colors[0],neededTime[0]]]
        for i in range(1,n):
            if stack[-1][0]==colors[i]:
                if stack[-1][1]<neededTime[i]:
                    temp=stack.pop()
                    max_value+=temp[1]
                    stack.append([colors[i],neededTime[i]])
                else:
                    max_value+=neededTime[i]
            else:
                stack.append([colors[i],neededTime[i]])
        return max_value
            
class TestCase:
    def test_case_one(self):
        assert Solution().minCost("abaac",[1,2,3,4,5])==3
    def test_case_two(self):
        assert Solution().minCost("abc",[1,2,3])==0
    def test_case_three(self):
        assert Solution().minCost("aabaa",[1,2,3,4,1])==2
    def test_case_four(self):
        assert Solution().minCost("aaabbbabbbb",[3,5,10,7,5,3,5,5,4,8,1])==26
    
