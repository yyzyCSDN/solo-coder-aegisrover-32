from collections import deque

class MovingAverage:

    def __init__(self, n):
        if n <= 0:
            raise ValueError('window must be positive')
        self.n = n
        self.q = deque()
        self.total = 0.0

    def push(self, x):
        x = float(x)
        self.q.append(x)
        self.total += x
        if len(self.q) > self.n:
            self.total -= self.q.popleft()
        # Until the window is full, average over the samples actually seen.
        return self.total / len(self.q)
