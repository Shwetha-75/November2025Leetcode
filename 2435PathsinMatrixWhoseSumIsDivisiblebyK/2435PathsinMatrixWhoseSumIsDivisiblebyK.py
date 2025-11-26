class Solution:
    def __init__(self):
        self.count=0
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        self.helper(m,n,0,0,grid,grid[0][0],k)
        return self.count
    def helper(self,m:int,n:int,row:int,col:int,grid:list[list[int]],sum:int,k:int):
        if row==m-1 and col==n-1:
            if not sum%k:
                self.count+=1
            return 
        if col+1<n:
            self.helper(m,n,row,col+1,grid,sum+grid[row][col+1],k)
        if row+1<m:
            self.helper(m,n,row+1,col,grid,sum+grid[row+1][col],k)
class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[[0]*k for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    dp[i][j][grid[0][0]%k]=1
                    continue 
                value=grid[i-1][j-1]%k 
                for r in range(k):
                    prev_mod=(r-value+k)%k 
                    dp[i][j][r]=(dp[i-1][j][prev_mod]+dp[i][j-1][prev_mod])%(10**9+7) 
        return dp[m][n][0]          
class TestApp:
    def test_case_one(self):
        assert Solution().numberOfPaths([[5,2,4],[3,0,5],[0,7,2]],3)==2
    def test_case_two(self):
        assert Solution().numberOfPaths([[0,0]],5)==1
    def test_case_three(self):
        assert Solution().numberOfPaths([[7,3,4,9],[2,3,6,2],[2,3,7,0]],1)==10
    