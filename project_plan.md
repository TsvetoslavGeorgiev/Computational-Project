# Studying Exchange Rate Tree-Heterogeneity - Project Plan

- Comment: where it says "Figure" or "Prove it" or "demo it" below that means it need some actual results to show the idea.
    - might need a Figure, a compound figure, one or more tables, and possibly some further explanation
        - or a big caption
    - Each would be a section or subsection of the results
        - These need to be written ASAP
    - Figures and tables are *not counted* in the word limit
        - presumably you can have as many as you want
    - If there is not enough room, put it in the supplemental material (appendices)



## Introduction

- Make an intro into model-based phylogenetic inference and how model violations influence it.
    - Mostly citations
- Go more specifically into ERTH and CTH, explain how they are not taken into account in the most widely-used models. Focus on ERTH.
- Talk about total, marginal and internal symmetry and how they're connected to the above two.
- Explain sources of phylogenetic attraction (long branch, among-site comp het, compositional, and (new) exchange rate) 
- Explain how this study will address these problems.


## Results

### Detecting and modelling compositional and exchange rate tree heterogeneity

- Compositional tree-heterogeneity (CTH) is well known
    - Can measure it with a chi-squared test
        - However, that suffers from Type-II error
        - Can fix that problem using a null distribution made from simulations (Figure)
    - Can also measure it with marginal symm test (Figure)

- It is possible to have CTH that passes these tests (Figure)
    - That means it is possible to have true CTH, but undetected by these tests (Prove it)
        - these may be rare pathological cases 
    - However, we can *model* CTH, and show that it exists ("detect" it) that way
    - Like choosing a best model, JC vs GTR, we "detect" GTR-ness by modelling it
    - How to model it
        - different comp vectors over the tree
        - ML or Bayesian MCMC
    - So the way to illustrate the problem with the symmetry tests is to get some data that passes them but has CTH and some data that doesn't pass them but has CTH

- Exchange rate tree-heterogeneity (ERTH) is not well known
    - Internal symmetry does not measure it specifically
        - it measures "homogeneity" or lack thereof
    - Internal symm test certainly measures ERTH sometimes (need proof, ie results here)
        - but as with CTH it is possible to have true ERTH that is undetectable by internal symm test (Prove it)
        - it might be interesting to look into this more (ie do original research on this, not reading about it)
    - Again as with CTH we can model it to measure it 
    - ERTH can be modelled by assigning different rate matrices to different nodes on a tree via NDRH.
    - As for CTH, the way to demo the problem with the symmetry tests is to show that data proven to have ERTH via modelling may or may not pass the test

### Phylogenetic attraction by ERTH

- It is well appreciated that CTH can cause problems with tree reconstruction
    - compositional attraction
    - It can be shown that ERTH can also cause attraction (cite Peter)
        - use simulated data (demo it, Figure) 
    

### Detecting ERTH in real datasets
- ??? 
- Use DNA alignments, as they would be faster
- The alignments need to be small, both in number of taxa and number of sites
- analyse with iqtree, p4 with gtr, ndch2, ndrh
- It is unknown if attraction due to ERTH is a problem in real data
    - So get some real data that when modelled with ERTH gives a different tree
    - Should there be quantitative comparison of the trees? -- Peter thinks not needed

- **Hopefully you have started analysing real datasets by now, if only with iqtree or mrbayes**



## Talk
- Several slides to mirror intro topics, for a more general audience. Explain the most common model assumptions, why they're not always met.
- Make sure to explain well what ERTH and CTH constitute. Then about the symmetries.
- Explain as simple as possible why a priori tree provision is a limitation and how it has been partially overcome.
- What was done in this study?
- How was it done? P4 was used, what was modelled in it, what else was done, with what aim.
- Describe results without getting too technical, provide some graphical representation.
- How has all this brought things forward, what has it shown?
- Why is this significant? How can it be used?
- What questions remain?
