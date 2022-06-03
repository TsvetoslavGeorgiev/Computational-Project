# Read in the checkpoints
cpr = McmcCheckPointReader(theGlob='*3000000')
cpr.writeProposalAcceptances()

mySkip = 1500
myModelNames = ['GTR+G', 'NDCH2+G', 'NDRH(2)+G', 'NDRH(4)+G', 'NDCH2+NDRH(4)+G']
count = 0
gtrg = 0

# Concatenate latter portions of likes for each model
print("\nMarginal likelihood estimates, and log BF")
for rNum in range(20):
    # Get the second column of numbers (zero-based column 1)
    if rNum % 4 == 0:
        n = Numbers('mcmc_likes_%i' % rNum, col=1, skip=mySkip)
    else:
        n.read('mcmc_likes_%i' % rNum, col=1, skip=mySkip)
    if (rNum + 1) % 4 == 0:
        # Estimate marg like
        ret = func.newtonRaftery94_eqn16(n.data)
        print("%10s" % myModelNames[count], end=' ')
        print("%10.3f" % ret, end=' ')
        if count != 0:
            diff = ret - gtrg
            print("%10.3f" % diff, end=' ')
        else:
            gtrg = ret
        count += 1
        print()
