# 이신우님 풀이

import sys
# 공사장 좌표(a, b, R)
a, b, r= map(int, input().split())
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
def showNoisy(arr):
    for cord in arr:
        x, y = cord
        if (((x - a)**2 + (y - b)**2) - r**2) < sys.float_info.epsilon:
            print('Nosiy')
        else:
            print('Silent')
showNoisy(arr)