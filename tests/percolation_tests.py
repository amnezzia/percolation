from nose.tools import *
from percolation.classes import *
import numpy as np

def test_initialization():

    grid = Percolation(10)
    assert_equal(grid.open.all() == False, True)
    assert_equal(grid.N, 10)
    assert_equal(grid.grid[99], 99)
    assert_equal(grid.size.all() == 1, True)

def test_open():

    grid = Percolation(10)
    assert_equal(grid.is_open(12), False)
    grid.set_open(12)
    assert_equal(grid.is_open(12), True)
    grid.set_open(1,0)
    assert_equal(grid.is_open(10), True)
    grid.set_open(9,9)
    assert_equal(grid.is_open(99), True)

def test_get_root():

    grid = Percolation(10)
    assert_equal(grid.get_root(12), 12)

def test_connect():

    grid = Percolation(10)
    grid.connect(12,13)
    assert_equal(grid.grid[12], 13)
    grid.connect(32,33)
    assert_equal(grid.grid[32], 33)
    grid.connect(12,14)
    assert_equal(grid.grid[14], 13)
    grid.connect(12,32)
    assert_equal(grid.grid[33], 13)
    assert_equal(grid.size[13], 5)

def test_percolates():
    grid = Percolation(5)
    grid.set_open(0,2)
    assert_equal(grid.size[0], 2)
    grid.set_open(1,2)
    assert_equal(grid.size[0], 3)
    grid.set_open(4,2)
    assert_equal(grid.size[24], 2)
    grid.set_open(3,2)
    assert_equal(grid.percolates(), False)
    grid.set_open(2,2)
    assert_equal(grid.percolates(), True)






