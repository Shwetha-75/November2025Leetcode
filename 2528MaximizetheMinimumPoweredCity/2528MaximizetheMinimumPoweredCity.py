class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        max_value=0
        # before adding k to it 
        n=len(stations)
        min_value=float('inf')
        for i in range(n):
            temp=0
            for j in range(i-r,i+r+1):
                if 0<=j<=n-1:
                    temp+=stations[j]
            min_value=min(min_value,temp)
        max_value=max(min_value,max_value)
        for m in range(n):
            curr=stations[m]
            min_value=float('inf') 
            stations[m]+=k 
            for i in range(n):
                 temp=0
                 for j in range(i-r,i+r+1):
                     if 0<=j<=n-1:
                         temp+=stations[j]
                 min_value=min(min_value,temp)
            max_value=max(max_value,min_value)
            stations[m]=curr 
        return max_value 
    
class Solution:
 

    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        low,high=0,k
        for station in stations:
            high+=station 
        ans=0
        while low<=high:
              mid=low+(high-low)//2
              if self.isPossible(mid,stations,r,k):
                  ans=mid 
                  low=mid+1
              else:
                  high=mid-1 
        return ans      

    def isPossible(self,mid:int,stations:list[int],r:int,k:int):
        n,sum=len(stations),0
        for i in range(r):
            sum+=stations[i]
        for i in range(n):
            if (i+r)<=n-1:
                sum+=stations[i+r]
            if (i-(r+1))>=0:
                sum+=stations[i-(r+1)]
            if sum<mid:
                if (mid-sum)>k: return False 
                if (i+r)<=(n-1):
                    stations[i+r]+=mid-sum 
                k-=mid-sum 
                sum=mid 
        return True
class TestApp:
    def test_case_one(self):
        assert Solution().maxPower([1,2,4,5,0],1,2)==5
    def test_case_two(self):
        assert Solution().maxPower([4,4,4,4],0,3)==4
