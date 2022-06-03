# The defaults for these values are much smaller.  These suggested
# changes may not be needed all the time, but seems to help for
# difficult data.
var.PIVEC_MIN = 1.e-6
var.RATE_MIN = 1.e-6
var.BRLEN_MIN = 1.e-5
var.GAMMA_SHAPE_MIN = 0.15


# Clean up debris from previous runs ...
#os.system("rm -f mcmc*")

# Assuming more than one run, we set the run number by calling this script as
# p4 sMcmc.py -- 0     # 0, 1, 2, ...
rNum = int(var.argvAfterDoubleDash[0])

read('../SRHtests-master/datasets/Bergsten_2013/alignment.nex')
d = Data()
t = func.readAndPop('../SRHtests-master/datasets/Bergsten_2013/finaltree.nex')
#myConstr = Constraints(taxNames=d.taxNames, rootConstraintTree=rTree)
#t = func.randomTree(taxNames=d.taxNames, biRoot=True, constraints=myConstr)
t.data = d


# Some settings for MCMC
nGen = 3000000
nSamples = 3000
sInterv = int(nGen / nSamples)
nCheckPoints = 3
cpInterv = int(nGen / nCheckPoints)

if rNum >= 0 and rNum <= 3:
    # Set up GTR+G model first
    t.newComp(free=1, spec='empirical', symbol='-')
    t.newRMatrix(free=1, spec='ones')
    t.setNGammaCat(nGammaCat=4)
    t.newGdasrv(free=1, val=0.5)
    t.setPInvar(free=0, val=0.0)
    
    # Run Mcmc
    m = Mcmc(t, runNum=rNum, nChains=1, sampleInterval=sInterv, checkPointInterval=cpInterv)
    m.prob.eTBR = 0.0
    m.prob.local = 0.0
    m.prob.root2 = 0.0
    m.run(nGen)

if rNum >=4 and rNum <= 7:
    # This is for NDCH2
    # Define the model
    # Fully parameterise the comps, including a comp for the root
    for n in t.nodes:
        c = t.newComp(free=1, spec='empirical', symbol='-')
        t.setModelComponentOnNode(c, node=n, clade=0)
    t.newRMatrix(free=1, spec='ones')
    t.setNGammaCat(nGammaCat=4)
    t.newGdasrv(free=1, val=0.5)
    t.setPInvar(free=0, val=0.0)
    mp = t.model.parts[0]
    mp.ndch2 = True
    mp.ndch2_leafAlpha = 5
    mp.ndch2_internalAlpha = 5
    
    # Make an Mcmc object, and make a couple of adjustments for NDCH2
    m = Mcmc(t, runNum=rNum, nChains=1, sampleInterval=sInterv, checkPointInterval=cpInterv)
    m.prob.ndch2_internalCompsDirAlpha = 0.0
    m.prob.ndch2_leafCompsDirAlpha = 0.0
    m.prob.ndch2_internalCompsDir = 1.0
    m.prob.ndch2_leafCompsDir = 1.0
    m.prob.eTBR = 0.0
    m.prob.local = 0.0
    m.prob.root2 = 0.0
    m.run(nGen)

if rNum >= 8 and rNum <= 15:
    # Now set up NDRH first with two matrices
    t.newComp(free=1, spec='empirical', symbol='-')
    rA = t.newRMatrix(free=1, spec='ones')
    rB = t.newRMatrix(free=1, spec='ones')
    # and potentially with four matrices
    if rNum >= 12 and rNum <= 15:
        rC = t.newRMatrix(free=1, spec='ones')
        rD = t.newRMatrix(free=1, spec='ones')
    t.setNGammaCat(nGammaCat=4)
    t.newGdasrv(free=1, val=0.5)
    t.setPInvar(free=0, val=0.0)
    t.setModelComponentsOnNodesRandomly()
    
    # Run Mcmc
    m = Mcmc(t, runNum=rNum, nChains=1, sampleInterval=sInterv, checkPointInterval=cpInterv)
    m.prob.eTBR = 0.0
    m.prob.local = 0.0
    m.prob.root2 = 0.0
    m.run(nGen)

if rNum >= 16 and rNum <= 19:
# Now do NDCH2 and NDRH with four matrices
    for n in t.nodes:
        c = t.newComp(free=1, spec='empirical', symbol='-')
        t.setModelComponentOnNode(c, node=n, clade=0)
    rA = t.newRMatrix(free=1, spec='ones')
    rB = t.newRMatrix(free=1, spec='ones')
    rC = t.newRMatrix(free=1, spec='ones')
    rD = t.newRMatrix(free=1, spec='ones')
    t.setNGammaCat(nGammaCat=4)
    t.newGdasrv(free=1, val=0.5)
    t.setPInvar(free=0, val=0.0)
    mp = t.model.parts[0]
    mp.ndch2 = True
    t.setModelComponentsOnNodesRandomly()
    mp.ndch2_leafAlpha = 5
    mp.ndch2_internalAlpha = 5
    
    # Make an Mcmc object, and make a couple of adjustments for NDCH2
    m = Mcmc(t, runNum=rNum, nChains=1, sampleInterval=sInterv, checkPointInterval=cpInterv)
    m.prob.ndch2_internalCompsDirAlpha = 0.0
    m.prob.ndch2_leafCompsDirAlpha = 0.0
    m.prob.ndch2_internalCompsDir = 1.0
    m.prob.ndch2_leafCompsDir = 1.0
    m.prob.eTBR = 0.0
    m.prob.local = 0.0
    m.prob.root2 = 0.0
    m.run(nGen)
