# 5-1(append, pop만)

stack = []
count = 0

def process_stack(command) :

    if command[0] == "push" :
        global count
        stack.append(command[1])
        count += 1

    elif command[0] == "pop" :
        if count >= 1 :
            print(stack.pop())
            count -= 1
        else :
            print(-1)

    elif command[0] == "size" :
        print(count)

    elif command[0] == "empty" :
        if count == 0 :
            print(1)
        else :
            print(0)

    elif command[0] == "top" :
        if count >= 1 :
            print(stack[-1]) 
        else :
            print(-1)
                 

n = int(input())

for _ in range(n) :
    command = input().split(" ")
    process_stack(command)

