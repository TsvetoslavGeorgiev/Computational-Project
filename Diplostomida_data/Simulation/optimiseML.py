# The defaults for these values are much smaller.  These suggested
# changes may not be needed all the time, but seems to help for
# difficult data.
var.PIVEC_MIN = 1.e-6
var.RATE_MIN = 1.e-6
var.BRLEN_MIN = 1.e-5
var.GAMMA_SHAPE_MIN = 0.15

read('../alignment.nex')
d = Data()
d.compoSummary()

doRateHet = False # toggle
doCompHet = False # toggle

read('../finaltree.nex')
t = var.trees[0]
t.data = d

c1 = t.newComp(free=1, spec='empirical')
rA = t.newRMatrix(free=1, spec='ones')
if doRateHet:
    rB = t.newRMatrix(free=1, spec='ones')
    t.setModelComponentOnNode(rA, node=t.root, clade=True)
    t.setModelComponentOnNode(rB, node=t.node("B"), clade=False)
    t.setModelComponentOnNode(rB, node=t.node("C"), clade=False)
if doCompHet:
    c2 = t.newComp(free=1, spec='empirical')
    t.setModelComponentOnNode(c1, node=t.root, clade=True)
    t.setModelComponentOnNode(c2, node=t.root, clade=False)
t.setNGammaCat(nGammaCat=4)
t.newGdasrv(free=1, val=0.5)
t.setPInvar(free=0, val=0.0)

t.optLogLike()
#t.calcLogLike()

t.model.dump()
t.tPickle()

