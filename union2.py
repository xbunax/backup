import random
import numpy as np
import time
import matplotlib.pyplot as plt

class WeightedQuickUnionUF:
    def __init__(self, n):
        self.count = n
        self.size = [1 for i in range(n)]
        self.parent = [i for i in range(n)]

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.find(p) == self.find(q)

    def find(self, p):
        self.validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def validate(self, p):
        n = len(self.size)
        if (p < 0 or p >= n):
            raise Exception('Out of range!')

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] = self.size[rootQ] + self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] = self.size[rootP] + self.size[rootQ]


class Percolation:
    def __init__(self, N):
        self.Array = [[0 for i in range(N)] for j in range(N)]
        self.size = N
        self.UF = WeightedQuickUnionUF(N * N + 2)

    # open site (row i, column j) if it is not open already
    def Open(self, i, j):
        if self.Array[i][j] == 1:
            # print('('+str(i)+','+str(j)+') has already been open!')
            return
        else:
            self.Array[i][j] = 1
            # print('('+str(i)+','+str(j)+') is open now!')
            if i == 0:
                self.UF.union(0, i * self.size + j + 1)
            if i == self.size - 1:
                self.UF.union(self.size * self.size + 1, i * self.size + j + 1)
            if i != 0:
                if self.isOpen(i - 1, j):
                    self.UF.union(i * self.size + j + 1, (i - 1) * self.size + j + 1)
            if i != self.size - 1:
                if self.isOpen(i + 1, j):
                    self.UF.union(i * self.size + j + 1, (i + 1) * self.size + j + 1)
            if j != 0:
                if self.isOpen(i, j - 1):
                    self.UF.union(i * self.size + j + 1, i * self.size + j)
            if j != self.size - 1:
                if self.isOpen(i, j + 1):
                    self.UF.union(i * self.size + j + 1, i * self.size + j + 2)

    # is site (row i, column j) open?
    def isOpen(self, i, j):
        return self.Array[i][j] == 1

    # is site (row i, column j) full?
    def isFull(self, i, j):
        return self.UF.connected(0, i * self.size + j + 1)

    # does the system percolate?
    def percolates(self):
        return self.UF.connected(0, self.size * self.size + 1)


class PercolationStats:
    def __init__(self, N, T):
        self.threshold = []
        self.times = T
        for k in range(T):
            experiment = Percolation(N)
            count = 0
            while (not experiment.percolates()):
                block_list = []
                for i in range(N):
                    for j in range(N):
                        if not experiment.isOpen(i, j):
                            block_list.append(i * N + j)
                to_open = random.choice(block_list)
                to_open_j = int(to_open % N)
                to_open_i = int((to_open - to_open_j) / N)
                experiment.Open(to_open_i, to_open_j)
                count = count + 1
            self.threshold.append(count / (N * N))
        self.Array = np.array(self.threshold)

    def mean(self):
        return np.mean(self.Array)

    def stddev(self):
        return np.std(self.Array, ddof=1)

    def confidenceLow(self):
        return self.mean() - 1.96 * self.stddev() / (self.times ** 0.5)

    def confidenceHigh(self):
        return self.mean() + 1.96 * self.stddev() / (self.times ** 0.5)


if __name__ == '__main__':
    time_start = time.time()
    test = PercolationStats(20, 1)
    print(test.mean())
    time_end = time.time()
    print('totally cost', time_end - time_start)
