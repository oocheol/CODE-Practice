class Stack:
    def __init__(self, n):
        self.stack_list = [None for _ in range(n)]
        self.stack_size = 0
    
    def push(self, num):
        self.stack_list[self.size()] = int(num)
        self.stack_size += 1
    
    def pop(self):
        if self.size() > 0:
            last_val = self.top()
        
            self.stack_list[self.size()-1] = None
            
            self.stack_size -= 1
            return last_val
        
        return -1

    def size(self):
        return self.stack_size

    def empty(self):
        if self.size() > 0:
            return 0
        
        return 1

    def top(self):
        if self.size() > 0:
            return self.stack_list[self.size()-1]
        
        return -1

def run_cmd_with_stack(new_stack, cmd):
    cmd_type = cmd[0]
    # cmd_type, num = cmd

    if cmd_type == "push":
        _, num = cmd
        new_stack.push(num)
    elif cmd_type == "pop":
        print(new_stack.pop())
    elif cmd_type == "size":
        print(new_stack.size())
    elif cmd_type == "empty":
        print(new_stack.empty())
    elif cmd_type == "top":
        print(new_stack.top())
     
    return new_stack

n = int(input())
new_stack = Stack(n)

# new_stack.stack_list
# new_stack.stack_size

for _ in range(n):
    # "push 2".split() => ["push", "2"]
    # "size".split() => ["size"]
    command = input().split()
    new_stack = run_cmd_with_stack(new_stack, command)

    print(new_stack.stack_list)
    print(new_stack.stack_size)