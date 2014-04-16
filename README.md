percolation
===========

Simulating percolation threshold by weighted quick union algorithm with path compression

Inspired by programming assignments for Coursera course:<br>
https://class.coursera.org/algs4partI-004<br>
Description of the problem is here:<br>
http://coursera.cs.princeton.edu/algs4/assignments/percolation.html

#####How to use:


    >>>from percolation.classes import Sims

    >>>sim = Sims()
    >>>sim.sim_n(100, 10)
	10 simulations of 100x100 grid:
	Average percolation threshold:  0.59268
	Standard deviation:  0.0183070368984
	It took 3.29275798798 seconds.

	>>>sim.sim_n(1000, 1)
	1 simulations of 1000x1000 grid:
	Average percolation threshold:  0.590911
	Standard deviation:  0.0
	It took 33.1701509953 seconds.
