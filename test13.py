jumsu = int (input("학점을 입력하세요 :"))

if jumsu > 90 :
    print("A입니다.")
else :
    if jumsu > 80 :
        print("B입니다.")
    else:
        if jumsu > 70 :
            print("C입니다.")
        else:
            if jumsu > 60 :
                print("D입니다.")
            else:
                print("F입니다.")