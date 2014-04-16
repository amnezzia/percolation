"""
Simulating percolation threshold
inspired by programming assignments for Coursera course:
https://class.coursera.org/algs4partI-004
description is here:
http://coursera.cs.princeton.edu/algs4/assignments/percolation.html
"""


import numpy as np
import time

class Percolation(object):
    """
    Percolation class for a square NxN grid
    open -  array that keeps track of which sites are open and which are still closed
            all sites are initially blocked
    grid -  keeps track of what site this site is connected to
    size -  number of sites for which this site is a root
    open_count - how many sites are open

    """

    def __init__(self, N):

        self.N = N
        # all arrays are actually one-dimensional
        self.open = np.zeros(N ** 2).astype(bool)
        self.grid = np.arange(N ** 2)
        self.size = np.ones(N ** 2)
        # count of opened sites
        self.open_count = 0

    def print_arrays(self, which='all'):
        """
        Prints all or one arrays.
        options: 'all', 'open', 'connect', 'size'
        """
        if which == 'all' or which =='open':
            print "Open sites:"
            print self.open.reshape(self.N, self.N), "\n"
        if which == 'all' or which == 'connect':
            print "Connected to:"
            print self.grid.reshape(self.N, self.N), "\n"
        if which == 'all' or which == 'size':
            print "Cluster sizes:"
            print self.size.reshape(self.N, self.N), "\n"

    def make_connections(self, p):
        """
        For newly opened site checks neighboring sites
        and makes connections if they are open
        """
        # convert to double index
        i = p / self.N
        j = p % self.N

        # all first row cells connects to 0
        if i == 0:
            self.connect(p, 0)

        # all last row cells connects to N**2 - 1
        if i == (self.N - 1):
            self.connect(p, (self.N**2 - 1))

        # connect to open neighbors

        # if not the top row and top site is open
        if i > 0 and self.is_open(p - self.N):
            self.connect(p, p - self.N)
        # if not the bottom row and down is open
        if i < (self.N - 1) and self.is_open(p + self.N):
            self.connect(p, p + self.N)
        # if not first column and left is open
        if j > 0 and self.is_open(p - 1):
            self.connect(p, p - 1)
        # if not last column and right site is open
        if j < (self.N - 1) and self.is_open(p + 1):
            self.connect(p, p + 1)

    def set_open(self, *args):
        """
        Opens site.
        Can give one index for a flattened array,
        or two indexes for a square array.
        Also calls function to make connections with neighbors
        """
        if len(args) == 1:
            p = args[0]
        elif len(args) == 2:
            p = self.N * args[0] + args[1]

        self.open[p] = True
        self.open_count += 1

        self.make_connections(p)

    def is_open(self, p):
        """
        Checks if the site is open.
        """
        # check if p is within the array
        in_array = (p >= 0 and p < (self.N ** 2))
        # if yes and site is open
        if in_array and self.open[p]:
            return True
        else:
            return False

    def get_root(self, p):
        """
        Searches for the root of the tree where this site is connected
        """
        save = p
        while p != self.grid[p]:
            p = self.grid[p]

        # flatten the tree by reassign to the found root
        self.grid[save] = p

        return p

    def connect(self, p, q):
        """
        Connects two sites together
        """

        # find roots
        p_root = self.get_root(p)
        q_root = self.get_root(q)

        if p_root == q_root:
            pass
        else:
            # weighted approach
            if self.size[p_root] <= self.size[q_root]:
                self.grid[p_root] = q_root
                self.size[q_root] += self.size[p_root]
            else:
                self.grid[q_root] = p_root
                self.size[p_root] += self.size[q_root]

    def connected(self, p, q):
        """
        checks if two sites are connected
        """
        return self.get_root(p) == self.get_root(q)

    def percolates(self):
        """
        checks if the system percolates
        """
        return self.connected(0, self.N ** 2 - 1)



class Sims(object):
    """
    Functions to run simulations using the Percolation object
    Sims.simulate_one(N) - simulates one system of size NxN
    Sims.sim_n(N, n_times) - runs n_times simulation of NxN systems
    """
    def simulate_one(self, N):

        # Initialize all sites to be blocked.
        perc = Percolation(N)

        # create a random sequence
        seq = np.random.permutation(N ** 2)

        # Repeat the following until the system percolates:
        for i in seq:

            # Choose a site uniformly at random among all blocked sites.
            # Open the site
            perc.set_open(i)

            # check if percolates
            if perc.percolates():
                break

        return float(perc.open_count) / float(N**2)

    def sim_n(self, N, n_times):

        start_time = time.time()
        score = np.zeros(n_times)

        for i in range(n_times):
            score[i] = self.simulate_one(N)

        print "{1} simulations of {0}x{0} grid:".format(N, n_times)
        print "Average percolation threshold: ", score.mean()
        print "Standard deviation: ", score.std()
        print "It took {} seconds.".format(time.time() - start_time)


