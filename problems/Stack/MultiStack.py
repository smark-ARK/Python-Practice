class MultiStack:
    def __init__(self, stack_size):
        self.num_stacks=3
        self.list=[0] * (self.num_stacks * stack_size)
        self.sizes=[0]*self.num_stacks
        self.stack_size=stack_size

    def is_full(self, stack_num):
        if self.sizes[stack_num]==self.stack_size:
            return True
        else:
            return False
    def is_empty(self, stack_num):
        if self.sizes[stack_num] == 0:
            return True
        else:
            return False
        
    def push(self, value, stack_num):
        if self.is_full(stack_num):
            return 