# 재귀문제 - 진법 전환 1
# 재귀 사용

# 입력예제 1
# ZZZZZ 36
# 출력예제 1
# 60466175

whole_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, m = input().split()

def recursion(x, y):
    n = 0
    res = []
    