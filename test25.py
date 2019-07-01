#mySet1 = {1,2,3,4,5,5,5,6}
#mySet2 = {8,5,7,1,2,4,}
#print(mySet1 & mySet2)
#print(mySet1 | mySet2)
#print(mySet1 - mySet2)
#print(mySet1 ^ mySet2)



# numList = []
# for num in range(1,6,1) :
#     numList.append(num)
# print(numList)
#
# numList = [num for num in range(1,6,1)]
# print(numList)


oldList = ["짜장면","탕수육","단무지"]
newList = oldList[:]
print(newList)
oldList[0] = "짬뽕"
oldList.append("깐풍기")
print(newList)