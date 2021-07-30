class C_Que:
    def __init__(self):
        # self.array = [None] * n
        self.array = []
        self.f_idx = 0
        self.b_idx = 0

    def enQueue(self, num):
        if self.f_idx > 0 :
            self.
        
        self.array.append(int(num))
        self.b_idx += 1
        print(self.array)
        return self.array

    def deQueue(self):
        self.f_idx += 1
        
        return self.array.pop(0)

    def size(self):
        return self.b_idx - self.f_idx

    def is_empty(self):
        return self.size() == 0

c_queue_obj = C_Que()

c_queue_obj.enQueue(14)
c_queue_obj.enQueue(22)
c_queue_obj.enQueue(13)
c_queue_obj.enQueue(-6)
c_queue_obj.deQueue()
c_queue_obj.deQueue()
c_queue_obj.enQueue(9)
c_queue_obj.enQueue(20)
c_queue_obj.enQueue(5)