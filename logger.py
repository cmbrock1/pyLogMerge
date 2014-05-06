from scanner import *
MODE = 0
YEAR = 1
MONTH = 2
DAY = 3
TIMESTAMP = 4
USER = 5
ACTION = 6
COST = 7

def mergeLogs(log1,log2):
    i = 0
    j = 0
    mlog = []
    while (i < len(log1) and j< len(log2)):
        if (earlier(log1[i],log2[j])):
            mlog.append(log1[i])
            i += 1
        else:
            mlog.append(log2[i])
            j += 1
    for k in range(i,len(log1),1):
        mlog.append(log1[k])
    for k in range(j,len(log2),1):
        mlog.append(log2[k])
    return mlog

def earlier(r1,r2):
    if (r1[YEAR] < r2[YEAR]):
        return True
    elif(r1[YEAR] > r2[YEAR]):
        return False
    elif(r1[MONTH] > r2[MONTH]):
        return True
    elif(r1[MONTH] > r2[MONTH]):
        return False
    elif(r1[DAY] > r2[DAY]):
        return True
    elif(r1[DAY] > r2[DAY]):
        return False
    elif(r1[TIMESTAMP] > r2[TIMESTAMP]):
        return True
    elif(r1[TIMESTAMP] > r2[TIMESTAMP]):
        return False
    else:
        return False

def printLog(log):
    for i in range (0,len(log),1):
        printRecord(log[i])
        return None

def printRecord(r):
    print(
    r[MODE],
    r[YEAR],
    r[MONTH],
    r[DAY],
    r[TIMESTAMP],
    r[USER],
    r[ACTION],
    r[COST],
    )
    return None

def printCost(log):
    print("# $",sumCost(log),sep="")
    return None

def sumCost(log):
    total = 0
    for i in range(0,len(log),1):
        total += log[i][COST]
    return total
    
def readLog(fileName):
    s = Scanner(fileName)
    table = []
    r = readLogRecord(s)
    while(r != ""):
        table.append(r)
        r = readLogRecord(s)
    s.close()
    return table

def readLogRecord(s):
    mode = s.readchar()
    if (mode == ""): 
        return ""
    if(mode == "#"):
        s.readline()
        return readLogRecord(s)
    year = s.readint()
    month = s.readint()
    day = s.readint()
    timestamp = s.readtoken()
    user = s.readtoken()
    action = s.readstring()
    cost = s.readfloat()
    record = [None] * 8
    record[MODE] = mode
    record[YEAR] = year
    record[MONTH] = month
    record[DAY] = day
    record[TIMESTAMP] = timestamp
    record[USER] = user
    record[ACTION] = action
    record[COST] = cost
    return [mode,year,month,day,timestamp,user,action,cost]


