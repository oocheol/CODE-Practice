# 5, len, array 안쓰고

stack = []

def len1(x) : 
    count = 0
    for _ in x:
        count += 1
    return count

def process_stack(command) :
    
    if command[0] == "push" :
        stack.append(command[1])

    elif command[0] == "pop" :
        if len1(stack) >= 1 :
            print(stack.pop()) 
        else :
            print(-1)

    elif command[0] == "size" :
        print(len1(stack))

    elif command[0] == "empty" :
        if len1(stack) == 0 :
            print(1)
        else :
            print(0)

    elif command[0] == "top" :
        if len1(stack) >= 1 :
            print(stack[-1]) 
        else :
            print(-1)
                 

n = int(input())

for _ in range(n) :
    command = input().split(" ")
    process_stack(command)

