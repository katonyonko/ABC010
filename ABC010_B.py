import io
import sys

_INPUT = """\
6
3
5 8 2
9
1 2 3 4 5 6 7 8 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  n=int(input())
  a=list(map(int,input().split()))
  ans=0
  for i in range(n):
    while a[i]%2==0 or a[i]%3==2:
      ans+=1
      a[i]-=1
  print(ans)