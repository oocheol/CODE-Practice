def insertion_sort(num_list):
    bef_n_list = num_list.copy()

    for idx in range(1, len(bef_n_list)):
        print(f"{idx}번째 : {bef_n_list}")

        # 1)
        # now_idx = idx

        # while now_idx > 0 and bef_n_list[now_idx] < bef_n_list[now_idx-1]:
        #     # t = bef_n_list[idx]
        #     # bef_n_list[idx] = bef_n_list[idx-1]
        #     # bef_n_list[idx-1] = t

        #     bef_n_list[now_idx], bef_n_list[now_idx-1] = bef_n_list[now_idx-1], bef_n_list[now_idx]
        #     now_idx -= 1

        #     print(bef_n_list)

        # 2)
        for now_idx in range(idx, 0, -1):
            if bef_n_list[now_idx] >= bef_n_list[now_idx-1]:
                break

            bef_n_list[now_idx], bef_n_list[now_idx-1] = bef_n_list[now_idx-1], bef_n_list[now_idx]
            print(bef_n_list)

    return bef_n_list

def selection_sort(num_list):
    bef_n_list = num_list.copy()
    
    # min_idx = 0

    # for idx in range(len(bef_n_list)):
    #     if bef_n_list[idx] < bef_n_list[min_idx]:
    #         min_idx = idx

    # bef_n_list[0], bef_n_list[min_idx] = bef_n_list[min_idx], bef_n_list[0]

    # min_idx = 1

    # for idx in range(1, len(bef_n_list)):
    #     if bef_n_list[idx] < bef_n_list[min_idx]:
    #         min_idx = idx

    # bef_n_list[1], bef_n_list[min_idx] = bef_n_list[min_idx], bef_n_list[1]

    # ...

    for i in range(len(bef_n_list)):
        min_idx = i

        for idx in range(i, len(bef_n_list)):
            if bef_n_list[idx] < bef_n_list[min_idx]:
                min_idx = idx

        bef_n_list[i], bef_n_list[min_idx] = bef_n_list[min_idx], bef_n_list[i]
        print(bef_n_list)

    return bef_n_list

def bubble_sort():

    return []

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

# insertion_sorted_list = insertion_sort(num_list)
# print(" ".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort(num_list)
print(" ".join(map(str, selection_sorted_list)))

# bubble_sorted_list = bubble_sort()
# print(" ".join(map(str, bubble_sorted_list)))
