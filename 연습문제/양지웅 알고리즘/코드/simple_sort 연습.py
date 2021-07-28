# def insertion_sort(num_list):
#     a = []
#     n = 0
#     while n+1 < len(num_list):
#         if num_list[n] >= num_list[n+1]:
#             num_list[n], num_list[n+1] = num_list[n+1], num_list[n]
#             n += 1

#         else :
#             n += 1
                

#     return num_list

# def selection_sort(num_list):
#     n = 0
#     while n+1 < len(num_list):
#         a = num_list.index(min(num_list[n:]))
#         if num_list[n] >= num_list[a] :
#             num_list[n], num_list[a] = num_list[a], num_list[n]
#             n += 1
#         else :
#             n += 1


#     return num_list

# def selection_sort(num_list):
#     n = 0
#     while n+1 < len(num_list):
#         a = num_list.index(min(num_list[n:]))
#         num_list[n], num_list[a] = num_list[a], num_list[n]
#         n += 1

#     return num_list

def selection_sort(num_list):
    res = []
    
    for _ in range(len(num_list)):
        x = num_list.index(min(num_list))
        res.append(num_list.pop(x))
        
    return res

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

bubble_sorted_list = bubble_sort()
print(" ".join(map(str, bubble_sorted_list)))
