# forwardsim

Forward simulator for popgen

Intro
We will try to simulate the fate of a given number of lineages in a Wright-Fisher population across a given number of generations.
We will proceed in increasing levels of complexity:

1. Basic simulation loop with constant population size, no recombination and no mutation. The simplest of the models involves a population of size N haploid individuals that evolves under drift only for a given number gen of generations. In generation 0 (initial set of lineages), each lineage is unique in the population, so all lineages have the same frequency. Each individual in the next generation is drawn from 1 single parent in the previous generation. To generate the counts of each lineage in the next generation multinomial random sampling with replacement is invoked.
1.a) Input: 1D array of N lineages with counts 1.
1.b) Output: Nxgen array of lineage counts across generations, and list of remaining lineages in each generation.
1.c) Rationale: Forward-in-time coalescence process. In the beginning coalescence times are short because many lineages are in the game, as fewer lineages remain the coalescence time become longer. Eventually however only one lineage will survive.
1.d) Script: WFsimulator_simplest.py


2. Simulation with recombination. Except for the first generation, each haploid individual in any given generation is going to be a mosaic of an x number of lineages from the initial set of lineages. A recombination rate is required now.

3. Simulation with recombination and mutation.

In order to translate this to diploid populations, at the end of each simulation pairs of haplotypes will be randomly sampled without replacement.   

Notation
r stands for no recombination
R stands for recombination
u stands for lack of mutation
U stands for presence of mutation
