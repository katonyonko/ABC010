import io
import sys

_INPUT = """\
6
chokudai
sanagi
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  q 