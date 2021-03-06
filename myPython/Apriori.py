
def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataSet):
    C1=[]
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset,C1)

def scanD(D,Ck,minSupport,q):
    ssCnt={}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not can in ssCnt: ssCnt[can]=1
                else:ssCnt[can] += 1
    numItems=float(len(q))
    retList=[]
    supportData={}
    for key in ssCnt:
        support=ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key]=support
    return retList,supportData

