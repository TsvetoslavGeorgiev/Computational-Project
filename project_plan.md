Studying Exchange Rate Tree-Heterogeneity - Project Plan

Introduction
- Make an intro into model-based phylogenetic inference and how model violations influence it.
- Go more specifically into ERTH and CTH, explain how they are not taken into account in the most widely-used models. Focus on ERTH.
- Talk about total, marginal and internal symmetry and how they're connected to the above two.
- Explain how this study will address these problems.


Results
- If CTH is present in a dataset, this can often elude simple tests performed on the data alone; such as a chi-squared test of nucleotide contents with
a null distribution based on simulated data. Or a test of marginal symmetry. Modelling however can detect CTH. This is done by specifying more than one composition vector and allowing these vectors
to be assigned to various nodes on the tree ina a Bayesian framework, as in NDCH2.
- The presence of ERTH is similarly elusive. Internal symmetry, which should act as a proxy for ERTH, evidently does not, as Ababneh's test often fails to
detect cases of ERTH which are known to be present. Similarly to CTH, ERTH can be modelled by assigning different rate matrices to different nodes on a tree
via NDRH.
- To illustrate the problem with using simple data tests for CTH and ERTH, heterogeneous data can be simulated and then both tested and modelled. Examples will
be provided for cases in which the test detects the heterogeneity and in which it doesn't (while it's present in both cases, as evidenced by modelling). This will
be done both for CTH and ERTH. A case where both phenomena are present but symmetry tests detect neither will also be provided to evidence the need to
always test for presence of these phenomena by modelling. Include figure(s) here (but what kind?), also a table for the numerical results.
-To include ERTH in phylogenetic models is important because if its presence is unaccounted for, it could bias inferences. But how much? This can be tested
by analysing the same data with a rate tree-homogeneous model and comparing the trees. Or rather, take the true tree and see what likelihoods there are for the data
under the two different models? I think the best idea would be to take a simple tree, simulate data on it under different scenarios of rate heterogenety over the
tree and then produce a tree with that data using a rate tree-homogeneous model (analogous to the github chapter). But how to produce the "tree based on composition"
analogue, i.e. the tree based on exchange rates?



Talk
- Several slides to mirror intro topics, for a more general audience. Explain the most common model assumptions, why they're not always met.
- Make sure to explain well what ERTH and CTH constitute. Then about the symmetries.
- Explain as simple as possible why a priori tree provision is a limitation and how it has been partially overcome.
- What was done in this study?
- How was it done? P4 was used, what was modelled in it, what else was done, with what aim.
- Describe results without getting too technical, provide some graphical representation.
- How has all this brought things forward, what has it shown?
- Why is this significant? How can it be used?
- What questions remain?
