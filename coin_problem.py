def getMinChange(changeList, changeAmt, minList, coinInfo):
    # count = 0
    for change in range(changeAmt + 1):
        minCoin = change
        info = 1
        # count = count + 1
        redefinedChangeList = [ i for i in changeList if i <= change]
        for changeOpt in redefinedChangeList:
            # count = count + 1
            if minList[change - changeOpt] + 1 < minCoin:
                minCoin = minList[change - changeOpt] + 1
                info = changeOpt

        minList[change] = minCoin
        coinInfo[change] = info
    print (minList)
    print (coinInfo)
    return minList[change]

def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

def getActualUsedCoin(coinInfo, data):
    tempForChange = data
    while tempForChange > 0:
        print(coinInfo[tempForChange])
        tempForChange = tempForChange - coinInfo[tempForChange]


if __name__ == '__main__':
    changeList = [1,2,5, 21, 25]
    forChange = 11
    minList = [0]* (forChange+1)
    coinInfo = [0] * (forChange + 1)
    print(getMinChange(changeList, forChange, minList, coinInfo))
    print( getActualUsedCoin(coinInfo, 8))
    # print(recMC([1,5,10,25],63))



