# 최대값, 최소값 구하기

num_list = list(map(int, input().split()))

max_num = num_list[0]
min_num = num_list[0]

for num in num_list:

    if max_num < num:
        max_num = num

    if min_num > num:
        min_num = num

print(max_num)
print(min_num)