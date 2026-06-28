class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
            PACIFIC
        [1, 2, 2, 3, 5] A
        [3, 2, 3, 4, 4]
      P [2, 4, 5, 3, 1]
        [6, 7, 1, 4, 5]
        [5, 1, 1, 2, 4]
            ATLANTIC
        
        1. Start from all ocean facting boundaries.
        2. Do a DFS and add the positions to the set if we can visit those positions from each ocean.
        3. atl set will have all the positions visitable from atlantic ocean
        4. pac will have all the posistions visitable from pacific ocean.
        5. Take the intersection of the set, that is the result.

        Intuition:
        - Originally thought that we will have to iterate through each position and then check if they can reach to the ocean or not.
            - That way we would have to remember the path we started from otherwise could go in loops.
                - In the below matrix, if we start from 3, which is unreachable, we keep going in loop, unless we keep track of visited.
                - Even if we do keep track of visited, we must also keep track that we have exhausted all possible ways we can reach the shore.
                - That simply makes it complicated.
                    [5 5 5 5] 
                    [5 3 3 5]       3 -> 3
                    [5 3 3 5]       ^    v    We go round and round.
                    [5 5 5 5]       3 <- 3
        - Hence we do a backtrack from shores and see what places can we reach and only remember the valid postions.
        """
        ROW, COL = len(heights), len(heights[0])
        atl = set()
        pac = set()


        def dfs(row, col, visited: set, prev_height: int):
            if (row, col) in visited or row<0 or col<0 or row>=ROW or col>=COL or heights[row][col] < prev_height:
                return
            
            visited.add((row, col))
            dfs(row-1, col, visited, heights[row][col])
            dfs(row+1, col, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
        
        for c in range(0, COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW-1, c, atl, heights[ROW-1][c])
            
        
        for r in range(0, ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL-1, atl, heights[r][COL-1])


        return list(atl.intersection(pac))


if __name__ == "__main__":
    req = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(Solution().pacificAtlantic(req))