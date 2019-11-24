class Queue(object):
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x):
        while self.pop_stack:
            self.push_stack.append(self.pop_stack.pop())
        self.push_stack.append(x)

    def pop(self):
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self):
        return not bool(self.push_stack) and not bool(self.pop_stack)


if __name__ == '__main__':
    import Test

    q = Queue()
    q.push(1)
    q.push(2)
    Test.equal(1, q.pop())
    q.push(3)
    q.push(4)
    Test.equal(False, q.empty())
    Test.equal(2, q.pop())
    Test.equal(3, q.pop())
    Test.equal(4, q.pop())
    Test.equal(True, q.empty())
