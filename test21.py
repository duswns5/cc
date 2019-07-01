list1 =[]
list2 =[]
list3 =[]
value = 0

for i in range (0,4,1) :
    for j in range (1,5,1) :
        value = value + 3
        for k in range (1,10) :
            result = str("%d X %d = %d"%(value,k,value*k))
            list1.append(result)
        list2.append(list1)
        list1 = []
    list3.append(list2)
    list2 = []
    print (list3)
    print ("")
