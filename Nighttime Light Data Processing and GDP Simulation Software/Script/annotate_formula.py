def computeAll(*argList):
 operatorList = []
 dstList = []
 index = 0
 
 for subList in argList:
    if(len(operatorList) == 0):
        operatorList = subList
        continue
    operator = operatorList[index]
    if(len(dstList) == 0):
       dstList = subList
    else:
        for offset in range(0, len(subList)):
          try:
            if operator == "+":
               dstList[offset] += subList[offset]
            if (operator == "-"):
               dstList[offset] -= subList[offset]
            if (operator == "*"):
               dstList[offset] *= subList[offset]
            if (operator == "/"):
               dstList[offset] /= subList[offset]
          except:
            dstList[offset] = subList[offset]
            break
        index+=1

 for index in range(0, len(dstList)):
     dstList[index] = str(dstList[index])

 return dstList


def computeSingle(*argList):

 operatorList = []
 
 for subList in argList:
     
    if(len(operatorList) == 0):
        operatorList = subList
        continue

    tmpValue = subList[0]
    for offset in range(1, len(subList)):
      operator = operatorList[offset-1]
      try:
        if operator == "+":
           tmpValue += subList[offset]
        if (operator == "-"):
           tmpValue -= subList[offset]
        if (operator == "*"):
           tmpValue *= subList[offset]
        if (operator == "/"):
           tmpValue /= subList[offset]
      except:
        tmpValue = subList[offset]
        break
    
    resultValue = str(tmpValue)
    break

 return resultValue

if __name__== '__main__':
    print("-------main-------")
else:
    print("-------module-------")


