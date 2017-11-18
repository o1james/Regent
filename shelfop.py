SourceList = "tape_list_sorted.TPeXOcvU"
shelfFile = "shelved_tapes_test"
tapeList = []

def getTapeList(numTapes):

    with open(SourceList,'r') as sL:
       fullFile = sL.readlines()
       for i in range(numTapes):
           line = fullFile[i]
           volser = line.split(":")[0]
           SClass = line.split()[1]
           writeDate = line.split()[3]
           writeTime = line.split()[4]
           readDate = line.split()[5]
           readTime = line.split()[6]
           state = line.split()[7]
           numFiles = line.split()[8]
           line = volser + ',' + SClass + ',,,,,' + writeDate + "," + writeTime + ',' + readDate + ',' + readTime + ',' + state + ',' + numFiles +'\n'
           tapeList.append(line)

    with open(SourceList,'w') as sLNew:
        sLNew.writelines(fullFile[numTapes:])

    return(tapeList)

def getCabinetDrawer():
    cabinetDrawerCol = [0,0,0]
    incCab,incDrw,incCol = False,False,False
    with open(shelfFile) as sF:
        sFList = sF.readlines()
        for line in sFList:
            for i in range(2):
                if line[1+2] > cabinetDrawerCol[i]:
                    cabinetDrawerCol = 


    cabinetDrawerCol = [1,5,2]
    return(cabinetDrawerCol)

def addCDCNum(tapeEntry):
    cabinetDrawerCol = getCabinetDrawer()
    tapeEntry[2:5] = cabinetDrawerCol[0:3]
    return(tapeEntry)

def addToFile(tapeLine):
    thisEntry = ''
    for i in range(len(tapeLine) - 1):
        thisEntry = thisEntry + str(tapeLine[i]) + ","
    thisEntry = thisEntry + tapeLine[-1]
    with open(shelfFile,"a+") as shF:
        shF.write(str(thisEntry))

def fillCol(tapeList):
    slot = 1
    for tape in tapeList:
        tapeEntry = (tape.split(','))
        tapeEntry = addCDCNum(tapeEntry)
        tapeEntry[5] = slot
        addToFile(tapeEntry)
        slot += 1

tapeList = getTapeList(25)
fillCol(tapeList)
