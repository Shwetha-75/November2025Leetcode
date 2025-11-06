import heapq

class Solution:
    def __init__(self):
        self.uf=[]
    # Slight modification on UF find operation as soon we found the parent we need to resign it again
    def find(self,x:int):
        if self.uf[x]!=x:
            self.uf[x]=self.find(self.uf[x])
        return self.uf[x]   
    # rather than assigning the the parent_i to parent_j 
    # assigning smaller one to be the parent of larger one, 
    # so that is station x goes offline it would be easy 
    # to pick the smaller available station
    
    def join(self,i:int,j:int):
        parent_i=self.find(i)
        parent_j=self.find(j)
        if parent_i<parent_j:
            self.uf[parent_j]=parent_i
        elif parent_i>parent_j:
            self.uf[parent_i]=parent_j
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        self.uf=[i for i in range(c+1)]
        hash_map={}
        for connection in connections:
            self.join(connection[0],connection[1])
        for x in range(1,c+1):
            root=self.find(x)
            if root not in hash_map:
                hash_map[root]=[]
            heapq.heappush(hash_map[root],x)   
        
        set_map=set(i for i in range(1,c+1))
        ans=[]
        for query in queries:
            if query[0]==2:
                if query[1] in set_map:
                    set_map.remove(query[1])
            else:
                # if station x is offline  
                if query[1] not in set_map:
                #    find the near by station smallest one such that 
                   curr_connection=hash_map[self.uf[query[1]]]
                   while curr_connection and curr_connection[0] not in set_map:
                       heapq.heappop(curr_connection)
                   if curr_connection:
                       ans.append(curr_connection[0])
                   else:
                       ans.append(-1)
                else:
                    ans.append(query[1])
                   
        return ans 

class TestApp:
    def test_case_one(self):
        assert Solution().processQueries(5,[[1,2],[2,3],[3,4],[4,5]],[[1,3],[2,1],[1,1],[2,2],[1,2]])==[3,2,3]
    def test_case_two(self):
        assert Solution().processQueries(3,[],[[1,1],[2,1],[1,1]])==[1,-1] 
    def test_case_three(self):
        assert Solution().processQueries(1,[],[[1,1],[2,1],[2,1],[2,1]])==[1]                  
    def test_case_four(self):
        assert Solution().processQueries(2,[[2,1]],
        [[1,1],[1,2],[2,2],
         [2,1],[2,2],[2,2],
         [2,1],[1,1],[2,2],
         [2,1],[1,1],[2,1],
         [2,2],[1,1],[1,2],
         [1,1],[1,1],[2,1],
         [1,1],[2,2],[2,2],
         [2,1],[1,2],[2,2],
         [1,1],[2,1],[2,2],
         [2,2],[1,1],[2,2]])==[1,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    def test_case_five(self):
        assert Solution().processQueries(2,[[1,2]],[
            [1,2],[2,1],[1,2],
            [1,1],[2,2],[1,2],
            [2,2],[1,1],[1,1],
            [2,1],[1,2],[1,2],
            [1,1],[2,1],[1,1],
            [1,1],[1,1],[2,1],
            [2,1],[2,1],[1,2],
            [2,1],[2,2],[1,2],
            [1,1],[2,2],[2,1],
            [2,2]])==[2,2,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    def test_case_six(self):
        assert Solution().processQueries(2,[[1,2]],[[1,1],[1,2],[1,2],[2,2],[2,2],[1,1],[1,2],[1,1]])==[1,2,2,1,1,1]
    def test_case_seven(self):
        assert Solution().processQueries(3,[[2,3],[1,2],[1,3]],[
            [1,1],[1,2],[1,2],
            [1,3],[1,3],[1,1],
            [2,3],[1,1],[2,2],
            [2,2],[1,2],[1,3],
            [2,1],[2,1],[1,3],
            [2,1],[2,3],[1,3],
            [1,3],[2,2],[1,1],
            [2,2],[1,2],[1,1],
            [1,2],[1,3],[1,2],
            [1,3],[2,2],[2,2],
            [2,3],[1,3],[1,2],
            [2,3],[1,2],[2,3],
            [2,3],[2,2],[2,2],
            [1,1],[2,3],[1,1]])==[1,2,2,3,3,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]                   
                    