class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        count=2 
        intervals.sort(key=lambda x:x[1])
        for i in range(1,len(intervals)):
            prev,curr=intervals[i-1],intervals[i] 
            if prev[1]-curr[0]==0 or prev[1]-curr[0]==1:
                count+=1
            elif prev[1]-curr[0]<0:
                count+=2
        return count 

class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],x[1]))
        p1,p2=float('-inf'),float('-inf')
        n,ans=len(intervals),0
        for interval in intervals:
            start,end=interval
            if start<=p1:
                continue 
            if start>p2:
                ans+=2
                p2=end
                p1=p2-1 
            else:
                ans+=1
                p1=p2 
                p2=end  
        return ans
                
           

class TestApp:
    def test_case_one(self):
        assert Solution().intersectionSizeTwo([[1,3],[3,7],[8,9]])==5
    def test_case_two(self):
        assert Solution().intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]])==3
    def test_case_three(self):
        assert Solution().intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]])==5
    def test_case_four(self):
        assert Solution().intersectionSizeTwo([[1,3],[3,7],[5,7],[7,8]])==4
