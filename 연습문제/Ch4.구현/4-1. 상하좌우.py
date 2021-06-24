# 구현 예제 문제 4-1
# 상하좌우

n = int(input())
x, y = 1, 1

goal = input().split()

# L, R, U, D 구현

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L','R','U','D']

for s in goal :
    for i in range(len(move)) :
        if s == move[i] :
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue

    x, y = nx, ny

print(x, y)