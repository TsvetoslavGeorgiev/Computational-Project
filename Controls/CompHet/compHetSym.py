nTax = 10
tNames = list("ABCDEFGHIJ")
a = func.newEmptyAlignment(dataType='dna', taxNames=tNames, length=2000)
d = Data([a])

doRateHet = False
doCompHet = True

myBrLen = 1.0

t = func.readAndPop("(A,(B,(((C,D),(E,F)),(G,(H,(I,J))))));")
t.taxNames = tNames
for n in t.iterLeavesNoRoot():
    n.br.len = myBrLen
intNodes = [2, 4, 5, 6, 9, 12, 14, 16]
for i in intNodes:
    n = t.node(i)
    n.br.len = 0.2

# t.draw()

t.data = d
c1 = t.newComp(free=0, spec='equal')
rA = t.newRMatrix(free=0, spec='specified', val=[1,2,3,4,5,6])
if doRateHet:
    rB = t.newRMatrix(free=0, spec='specified', val=[4,5,6,1,2,3])
    t.setModelComponentOnNode(rA, node=t.root, clade=True)
    t.setModelComponentOnNode(rB, node=t.node("B"), clade=False)
    t.setModelComponentOnNode(rB, node=t.node("C"), clade=False)
if doCompHet:
    c2 = t.newComp(free=0, spec='specified', val=[0.3,0.2,0.3])
    c3 = t.newComp(free=0, spec='specified', val=[0.2,0.3,0.2])
    t.setModelComponentOnNode(c1, node=t.root, clade=True)
    t.setModelComponentOnNode(c2, node=6, clade=True)
    t.setModelComponentOnNode(c3, node=t.node('H'), clade=False)
# No asrv
t.setNGammaCat(nGammaCat=1)
#t.newGdasrv(free=0, val=0.5)
t.setPInvar(free=0, val=0.0)

t.simulate()

a.writePhylip("dCompHet.phy")

