nTax = 117
t = func.readAndPop('t0.p4_tPickle')
a = func.newEmptyAlignment(dataType='dna', taxNames=t.taxNames, length=1244)
d = Data([a])

#t.draw()

t.data = d


t.simulate()

d.writeNexus('alignment.nex')


