from collections import defaultdict 
from functools import reduce 
INF = 10**5 
def solve(p,A,trie): 
    f = [0]*(p+1) 
    f[p] = 0 
    for i in range(p-1,-1,-1): 
        f[i] = f[i+1]+min(A[i][0],A[i][1]) 
    def dfs(now,i,rt): 
        if "0" in rt and "1" in rt: 
            return min(dfs(now+A[i][0],i+1,rt["0"]),dfs(now+A[i][1],i+1,rt["1"])) 
        if "0" in rt: 
            return min(now+A[i][1]+f[i+1],dfs(now+A[i][0],i+1,rt["0"])) 
        if "1" in rt: 
            return min(now+A[i][0]+f[i+1],dfs(now+A[i][1],i+1,rt["1"])) 
        return INF 
    return dfs(0,0,trie) 


if __name__ == "__main__":
    Trie = lambda:defaultdict(Trie) 
    END = True 
    t = int(input()) 
    for round in range(1,t+1): 
        n,m,p = map(int,input().split()) 
        A = [[0,0] for _ in range(p)] 
        trie = Trie() 
        for _ in range(n): 
            string = input() 
            for i,c in enumerate(string): 
                if c=='1': 
                    A[i][0] += 1 
                else: A[i][1] += 1 
        for _ in range(m): 
            reduce(dict.__getitem__,input(),trie)[END] = 1 
        print("Case #%d: %d"%(round,solve(p,A,trie))) 

