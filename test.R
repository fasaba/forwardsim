### simple simulator for haploid lineages - using multinomial
### population size is constant

### population size i sN
N = 100


timeToOneLineage = c()
for (replicate in 1:1000){
### counts of each lineage - stored in n
n = rep(1, N)
n = matrix(n, ncol=1)
survivinglineages = sum(n[,1] != 0)

## simulation of frequencies of each lineage for 100 genrations
for (gen in 1:1000) {
  ## compute frequency in current generation
  frequency_current = n[,gen]/sum(n[,gen])
  ## get counts for each of these lineages in the next generation
  counts_next = as.vector(rmultinom(1, prob=frequency_current, size=N))
  ## update the count matrix with counts of the next generation
  n = cbind(n, counts_next)
  survivinglineages = c(survivinglineages, sum(counts_next != 0))
}
timeToOneLineage = c(timeToOneLineage, which(survivinglineages == 1)[1])
print(replicate)
}

rpois()
