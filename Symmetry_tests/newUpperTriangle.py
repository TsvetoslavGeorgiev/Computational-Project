def SymmTestUpperTriangle(self):          
    QB, QS, QR, PB, PS, PR = self.matchedPairsTests()
    dm = self.pDistances()

    newPB = list()
    newPS = list()
    newPR = list()

    for i in range(len(PB.matrix)):
        for j in range(i+1, len(PB.matrix[0])):
            newPB.append(PB.matrix[i][j])
            newPS.append(PS.matrix[i][j])
            newPR.append(PR.matrix[i][j])

    return newPB, newPS, newPR

Alignment.SymmTestUpperTriangle = SymmTestUpperTriangle
del(SymmTestUpperTriangle)
