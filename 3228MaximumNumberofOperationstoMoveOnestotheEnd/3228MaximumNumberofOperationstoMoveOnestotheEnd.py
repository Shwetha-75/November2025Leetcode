class Solution:
    def maxOperations(self, s: str) -> int:
        n=len(s)
        ans,impact,startIndex,count_one=0,1,n-1,0
        if n==1:
            return 0
        for char in s:
            if char=="1":
                count_one+=1
        if count_one==n:
            return 0
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                startIndex=i
                break 
        i=startIndex
        while i>=0:
            if s[i]=='0': 
                i-=1
                continue
            count=0 
            for j in range(i,-1,-1):
                if s[j]=='1':
                    count+=1
                else:
                    break 
            ans+=count*impact
            impact+=1
            i=j-1
        return ans 
class TestApp:
    def test_case_one(self):
        assert Solution().maxOperations("1001101")==4
    def test_case_two(self):
        assert Solution().maxOperations("000111")==0
    def test_case_three(self):
        assert Solution().maxOperations("110110111")==6
    def test_case_four(self):
        assert Solution().maxOperations("110")==2
    def test_case_five(self):
        assert Solution().maxOperations("111111")==0
    def test_case_six(self):
        assert Solution().maxOperations("0001111")==0
    