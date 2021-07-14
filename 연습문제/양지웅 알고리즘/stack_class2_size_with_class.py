class Stack:
    def __init__(self):
        self.stack = []
        self.stack_size = 0

        # self.stack = [None] * n
        
    def push(self, num):
        self.stack.append(int(num)) 
        # self.stack += [int(num)]의 경우 시간복잡도가 올라갈 수 있음!!(사용 지양)
        
        self.stack_size += 1
        
    
    def pop(self):
        if self.size() > 0:
            self.stack_size -= 1
            return self.stack.pop()
        
        return -1
    
    def size(self):
        return self.stack_size

    def empty(self):
        if self.size() > 0:
            return 0
        
        return 1

    def top(self):
        if self.size() > 0:
            return self.stack[self.size()-1]
        
        return -1

def run_cmd_with_stack(cmd, stack_lst):
    cmd_type = cmd[0]
    
    if cmd_type == "push":
        _, num = cmd
        stack_lst.push(num)
    elif cmd_type == "pop":
        print(stack_lst.pop())
    elif cmd_type == "size":
        print(stack_lst.size())
    elif cmd_type == "empty":
        print(stack_lst.empty())
    elif cmd_type == "top":
        print(stack_lst.top())
    
    return stack_lst

stack_lst = Stack()
# stack_lst.stack
# stack_lst.stack_size

n = int(input())

for _ in range(n):
    command = input().split()
    stack_lst = run_cmd_with_stack(command, stack_lst)