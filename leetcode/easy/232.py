class MyQueue:
    def __init__(self):
        self.stack_a, self.stack_b = [], []

    def push(self, x: int) -> None:
        self.stack_a.append(x)

    def pop(self) -> int:
        num_item = len(self.stack_a) - 1
        for _ in range(num_item):
            self.stack_b.append(self.stack_a.pop())

        popped = self.stack_a.pop()

        num_item = len(self.stack_b)
        for _ in range(num_item):
            self.stack_a.append(self.stack_b.pop())

        return popped

    def peek(self) -> int:
        return self.stack_a[0]

    def empty(self) -> bool:
        return len(self.stack_a) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()