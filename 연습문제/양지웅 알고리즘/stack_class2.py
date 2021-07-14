def run_cmd_with_stack(cmd, stack):
    cmd_type = cmd[0]
    
    if cmd_type == "push":
        _, num = cmd
        stack.append(int(num))
    elif cmd_type == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

        # try:
        #     print(stack.pop())
        # except IndexError:
        #     print(-1)
    elif cmd_type == "size":
        print(len(stack))
    elif cmd_type == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif cmd_type == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    
    return stack

stack = []
n = int(input())

for _ in range(n):
    # "push 2".split() => ["push", "2"]
    # "size".split() => ["size"]
    # .split(" ")
    command = input().split()
    stack = run_cmd_with_stack(command, stack)