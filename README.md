# forwardsim

Forward simulator for popgen

Intro
We will try to simulate the fate of a given number of lineages in a Wright-Fisher population across a given number of generations.
We will proceed in increasing levels of complexity:

1. Basic simulation loop with constant population size, no recombination and no mutation

The simplest of the models involves a population of size N haploid individuals that evolves under drift only for a given number gen of generations. In generation 0 (initial set of lineages), each lineage is unique in the population, so all lineages have the same frequency. Each individual in the next generation is drawn from 1 single parent in the previous generation. To generate the counts of each lineage in the next generation multinomial random sampling with replacement is invoked.
1.a) Input: 1D array of N lineages with counts 1.
1.b) Output: Nxgen array of lineage counts across generations, and list of remaining lineages in each generation.
1.c) Rationale: Forward-in-time coalescence process. In the beginning coalescence times are short because many lineages are in the game, as fewer lineages remain the coalescence time become longer. Eventually however only one lineage will survive.
1.d) Script: WFsimulator_simplest.py


2. Simulation with recombination

The first generation, gen0 is a fixed list of haplotypes. To generate the subsequent generations, haplotypes will be created by drawing parents from the previous generation given a recombination rate scaled by the length of the haplotype. Entities are still haploid, but recombination events are allowed and any given haplotype in any given generation can be a mosaic of several chunks of from different haplotypes in the immediately previous generation.

Class Haplotype will initialise and assign values to each haplotype of a generation, and the Generation class initialises the right number of haplotypes given a specified current population size. Class Simulation will produce a given number of generations given a set of initial haplotypes and a file specifying changes in population size along time.

A Simulation object should also have a deconvolve function able to return the lineages at the end of the simulation. Haplotypes in the final generation will be mosaics of regions from different haplotypes in the gen0, the initial pool of haplotypes. We can therefore track each tract of each haplotype all the way back to its very origin in gen0.



3. Simulation with recombination and mutation.

In order to translate this to diploid populations, at the end of each simulation pairs of haplotypes will be randomly sampled without replacement.   

Notation
r stands for no recombination
R stands for recombination
u stands for lack of mutation
U stands for presence of mutation
