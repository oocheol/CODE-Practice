# 5

stack = []

def process_stack(cmd) :
    cmd_type = cmd[0]
    if cmd_type == "push" :
        stack.append(cmd[1])

    elif cmd_type == "pop" :
        if len(stack) >= 1 :
            print(stack.pop()) 
        else :
            print(-1)

    elif cmd_type == "size" :
        print(len(stack))

    elif cmd_type == "empty" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    elif cmd_type == "top" :
        if len(stack) >= 1 :
            print(stack[-1]) 
        else :
            print(-1)
                 

n = int(input())

for _ in range(n) :
    cmd = input().split(" ")
    process_stack(cmd)

