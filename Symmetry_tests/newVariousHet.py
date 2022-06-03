nTax = 4
tNames = list('ABCD')
a = func.newEmptyAlignment(dataType='dna', taxNames=tNames, length=10000)
d = Data([a])

hetType = 'rate' #toggle between 'rate' and 'comp'

leafBrLen = 1.0
internalBrLen = 1.0 #toggle
t = func.readAndPop('(A,(B,(C,D)));')
t.taxNames = tNames
for n in t.iterLeavesNoRoot():
    n.br.len = leafBrLen
n = t.node(2)
m = t.node(4)
n.br.len = internalBrLen
m.br.len = internalBrLen

# t.draw()

t.data = d
c1 = t.newComp(free=0, spec='equal')
t.setModelComponentOnNode(c1, node=t.root, clade=True)
rA = t.newRMatrix(free=0, spec='ones')
t.setModelComponentOnNode(rA, node=t.root, clade=True)
if hetType == 'rate':
    rB = t.newRMatrix(free=0, spec='specified', val=[5,1,1,1,1,1])
    rC = t.newRMatrix(free=0, spec='specified', val=[1,5,1,1,1,1])
    t.setModelComponentOnNode(rB, node=t.node('A'), clade=False)
    t.setModelComponentOnNode(rB, node=t.node('B'), clade=False)
    t.setModelComponentOnNode(rB, node=t.node('C'), clade=False)
    t.setModelComponentOnNode(rC, node=t.node('D'), clade=False)
if hetType == 'comp':
    c2 = t.newComp(free=0, spec='specified', val=[0.2,0.3,0.2])
    c3 = t.newComp(free=0, spec='specified', val=[0.3,0.2,0.3])
    t.setModelComponentOnNode(c2, node=t.node('A'), clade=False)
    t.setModelComponentOnNode(c2, node=t.node('B'), clade=False)
    t.setModelComponentOnNode(c2, node=t.node('C'), clade=False)
    t.setModelComponentOnNode(c3, node=t.node('D'), clade=False)

# No asrv
t.setNGammaCat(nGammaCat=1)
#t.newGdasrv(free=0, val=0.5)
t.setPInvar(free=0, val=0.0)

os.system('rm -f NKResults_%s_%f*' % (hetType, internalBrLen))

for i in range(100):
    t.simulate()
    with open('NKResults_%s_%f_total.txt' % (hetType, internalBrLen), 'a') as f:
        for item in a.SymmTestUpperTriangle()[0]:
            f.write('%s ' % item)
        f.write('\n')
    with open('NKResults_%s_%f_marginal.txt' % (hetType, internalBrLen), 'a') as f:
        for item in a.SymmTestUpperTriangle()[1]:
            f.write('%s ' % item)
        f.write('\n')
    with open('NKResults_%s_%f_internal.txt' % (hetType, internalBrLen), 'a') as f:
        for item in a.SymmTestUpperTriangle()[2]:
            f.write('%s ' % item)
        f.write('\n')

f.close()
