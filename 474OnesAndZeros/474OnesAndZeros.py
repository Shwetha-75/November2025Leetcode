# Recursive

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        arr=[]
        for str_word in strs:
            count_one=count_zero=0 
            for char in str_word:
                if char=="1":
                    count_one+=1
                else:
                    count_zero+=1
            arr.append([count_zero,count_one])
        arr.sort(key=lambda x:(x[0],x[1]))
        res=[]
        print(arr)
        self.helper(0,len(arr),res,arr,[0,0,0])
        max_length=0
        for curr in res:
            if curr[0]<=m and curr[1]<=n:
                max_length=max(max_length,curr[2])
        return max_length 
    def helper(self,index:int,n:int,res:list[list[list[int]]],arr:list[list[int]],stack:list[int]):
        if index==n:
            res.append(stack[:])
            return 
        stack[0]+=arr[index][0]
        stack[1]+=arr[index][1]
        stack[2]+=1
        self.helper(index+1,n,res,arr,stack)
        stack[0]-=arr[index][0]
        stack[1]-=arr[index][1]
        stack[2]-=1
        self.helper(index+1,n,res,arr,stack)    
        
# Knapsack + 3D dynamic programming 
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        arr=[] 
        for word in strs:
            count_zero=count_one=0 
            for char in word:
                if char=="1":
                    count_one+=1
                else:
                    count_zero+=1
            arr.append([count_zero,count_one])
        dp=[[[-1]*(n+1) for _ in range(m+1)]for _ in range(len(arr))]
        return self.knapsack(arr,m,n,0,dp)

    def knapsack(self,arr:list[list[int]],m:int,n:int,index:int,dp):
        if index==len(arr) or (m==0 and n==0):
            return 0 
        if dp[index][m][n]!=-1:
            return dp[index][m][n]
        take=0
        if arr[index][0]<=m and arr[index][1]<=n:
            take=1+self.knapsack(arr,m-arr[index][0],n-arr[index][1],index+1,dp)
        skip=self.knapsack(arr,m,n,index+1,dp)
        dp[index][m][n]=max(skip,take)
        return dp[index][m][n]
class TestApp:
    def test_case_one(self):
        assert Solution().findMaxForm(["10","0001","111001","1","0"],5,3)==4
    def test_case_two(self):
        assert Solution().findMaxForm(["10","0","1"],1,1)==2
    def test_case_three(self):
        assert Solution().findMaxForm(["00","01","111"],2,3)==2
    def test_case_four(self):
        assert Solution().findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"],9,80)==17
    
