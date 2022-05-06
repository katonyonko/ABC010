import io
import sys

_INPUT = """\
6
1 1 8 2 2 4
1
4 5
1 1 8 2 2 6
1
4 5
1 1 8 2 2 5
1
4 5
7 7 1 1 3 4
3
8 1
1 7
9 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  txa,tya,txb,tyb,T,V=map(int,input().split())
  n=int(input())
  ans='NO'
  for i in range(n):
    x,y=map(int,input().split())
    if ((x-txa)**2+(y-tya)**2)**.5+((x-txb)**2+(y-tyb)**2)**.5<=T*V: ans='YES'
  print(ans)