# 큐 추가 문제(2) - 회전하는 큐

n, m = map(int, input().split())
a, b, c = map(int,input().split())

array = [x for x in range(1, n+1)]
print(array)
temp = [a, b, c]

array1 = array.copy()

    