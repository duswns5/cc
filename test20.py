i = 0
j = 0

while i < 9 :
    if i < 5 :
        j = 0
        while j < 4-i :
            print("",end = "  ")
            j = j+1
        j = 0
        while j < i*2+1 :
            print("\u2605",end = "")
            j = j+1
    else :
        j = 0
        while j < i-4 :
            print("",end = "  ")
            j = j+1
        j = 0
        while j < (9-i)*2-1 :
            print ("\u2605",end = "")
            j = j+1
    print()
    i = i+1
