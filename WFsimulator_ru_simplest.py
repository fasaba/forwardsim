
# coding: utf-8

# In[ ]:


### simple simulator for haploid lineages - using multinomial


# In[20]:


### population size is constant and equals N
N = 100


# In[21]:


import numpy as np


# In[22]:


for replicate in range(3):

# create an array of N lineages with equal counts in a population of size N
    n = np.array([1]*N)
    n.shape

# specify number of generations to simulate 
    gen_number = 100
    gen_range = range(gen_number)

# remaining lineages after each generation for each replicate
    remainingLines = list()
# simulation of frequencies of each lineage for gen_number generations
    for gen in gen_range:
        if gen==0:
    ## calculate lineages frequencies in current generation when array data is 1D
            frequency_current = n / np.sum(n)
    ## sample lineages from current to next generation and compute corresponding counts
            counts_next = np.random.multinomial(N, frequency_current)
    ## update the count matrix with counts of the next generation
            n = np.column_stack((n, counts_next))
    
        else:
    ## calculate lineages frequencies in current generation once array is multiD
            frequency_current = n[:,gen] / np.sum(n[:,gen])
    ## sample lineages from current to next generation and compute corresponding counts
            counts_next = np.random.multinomial(N, frequency_current)
    ## update the count matrix with counts of the next generation
            n = np.column_stack((n, counts_next))
        remainingLines.append(np.count_nonzero(n[:,gen]))
    print(remainingLines)

