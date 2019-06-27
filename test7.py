for i in range(1,6,1) :
    if i < 5 :
        j = 0
        for j in range (1,5-i,1) :
            print (" ",end = "")
        for j in range (1,i*2+1,1) :
            print ("*",end = "")
    else :
        for j in range (1,i-5,-1) :
            print (" ",end = "")
        for j in range (1,(5-i)*2-1,1) :
            print ("*",end = "")
    print("")
