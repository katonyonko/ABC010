import io
import sys

_INPUT = """\
6
4 2 3
2 3
0 1
1 2
1 3
4 1 4
3
0 1
0 2
1 3
2 3
10 3 11
7 8 9
0 1
0 2
0 3
0 4
1 5
2 5
5 6
6 7
6 8
3 9
4 9
6 2 6
4 5
0 1
0 2
1 3
2 3
3 4
3 5
4 3 3
1 2 3
1 2
1 3
2 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  # Ford-Fulkerson algorithm
  class FordFulkerson:
      def __init__(self, N):
          self.N = N
          self.G = [[] for i in range(N)]
  
      def add_edge(self, fr, to, cap):
          forward = [to, cap, None]
          forward[2] = backward = [fr, 0, forward]
          self.G[fr].append(forward)
          self.G[to].append(backward)
  
      def add_multi_edge(self, v1, v2, cap1, cap2):
          edge1 = [v2, cap1, None]
          edge1[2] = edge2 = [v1, cap2, edge1]
          self.G[v1].append(edge1)
          self.G[v2].append(edge2)
  
      def dfs(self, v, t, f):
          if v == t:
              return f
          used = self.used
          used[v] = 1
          for e in self.G[v]:
              w, cap, rev = e
              if cap and not used[w]:
                  d = self.dfs(w, t, min(f, cap))
                  if d:
                      e[1] -= d
                      rev[1] += d
                      return d
          return 0
  
      def flow(self, s, t):
          flow = 0
          f = INF = 10**9 + 7
          N = self.N 
          while f:
              self.used = [0]*N
              f = self.dfs(s, t, INF)
              flow += f
          return flow
  N,G,E=map(int,input().split())
  p=list(map(int,input().split()))
  ff=FordFulkerson(N+1)
  for i in range(G):
    ff.add_edge(p[i],N,1)
  for i in range(E):
    a,b=map(int,input().split())
    ff.add_multi_edge(a,b,1,1)
  print(ff.flow(0,N))