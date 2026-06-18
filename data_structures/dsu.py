""" 
Represents Disjoint Set Union Data Structure
"""

class DSU:
    def __init__(self, size: int):
        self.par = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]

    def connected(self, a, b) -> bool:
        return self.find(a) == self.find(b)
           
    def count(self, x) -> int:
        ...

    def find(self, x: int)-> int:
        par_x = self.par[x]
        if par_x == x:
            return x
        
        self.par[x] = self.find(par_x)
        return self.par[x]
    
    def union(self, a: int, b: int) -> None:
        king_a = self.find(a)
        king_b = self.find(b)

        if king_a == king_b:
            # already in same set:
            return
        
        rank_a = self.rank[a]
        rank_b = self.rank[b]

        if rank_a == rank_b:
            self.par[king_b] = king_a
            self.rank[king_a] += 1
        elif rank_a > rank_b:
            self.par[king_b] = king_a
        else:
            self.par[king_a] = king_b


if __name__ == "__main__":
    djs = DSU(4)
