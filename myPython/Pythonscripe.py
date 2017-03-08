import myPython.Apriori
dataSet=myPython.Apriori.loadDataSet()
print(dataSet)
dataSet=myPython.Apriori.loadDataSet()
C1=myPython.Apriori.createC1(dataSet)
D=map(set,dataSet)
q=list(D)
L1,suppData0=myPython.Apriori.scanD(D,C1,0.5,q)
print(L1)
