# 5

stack = []

def process_stack(command) :
    if command[0] == "push" :
        stack.append(command[1])

    elif command[0] == "pop" :
        if len(stack) >= 1 :
            print(stack.pop()) 
        else :
            print(-1)

    elif command[0] == "size" :
        print(len(stack))

    elif command[0] == "empty" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    elif command[0] == "top" :
        if len(stack) >= 1 :
            print(stack[-1]) 
        else :
            print(-1)
                 

n = int(input())

for _ in range(n) :
    command = input().split(" ")
    process_stack(command)

