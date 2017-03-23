numArray = []
baseArray = [1,2,3,4]
baseNum = 0
for i in baseArray:
    for j in baseArray:
        if j!=i :
            for k in baseArray:
                if k != i and k != j :
                    baseNum = i*100 + j*10 + k
                    numArray.append(baseNum)
print("一共能够生成%d个三位数: "%(len(numArray)))
print(numArray)
