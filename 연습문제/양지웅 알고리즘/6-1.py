# 6-1 class
class Que :
    def __init__(self) :
         self.que = []
         self.que_size = 0

    def push(self, num) :
        self.que.append(int(num))
        self.que_size += 1

    def pop(self) :
        if self.size() > 0 :
            self.a = []
            self.a.append(self.que[0])
            del self.que[0]
            self.que_size -= 1
            return self.a[0]
             
                       
        else :  
            return -1

    def size(self):
        return self.que_size

    def empty(self):
        if self.size() > 0:
            return 0
        
        return 1

    def front(self):
        if self.size() > 0 :
            return self.que[0]
        return -1
    
    def back(self):
        if self.size() > 0 :
            return self.que[-1]
        return -1
    
    
def run_cmd_with_que(cmd, stack_lst):
    cmd_type = cmd[0]
    
    if cmd_type == "push":
        _, num = cmd
        que_lst.push(num)
    elif cmd_type == "pop":
        print(que_lst.pop())
    elif cmd_type == "size":
        print(que_lst.size())
    elif cmd_type == "front":
        print(que_lst.front())
    elif cmd_type == "back":
        print(que_lst.back())
    elif cmd_type == "empty":
        print(que_lst.empty())
        
    return que_lst

que_lst = Que()
# stack_lst.stack
# stack_lst.stack_size

n = int(input())

for _ in range(n):
    x = input().split()
    que_lst = run_cmd_with_que(x, que_lst)