import test28
def para3_fucn(v1,v2,v3) :
    result = 0
    result = v1 + v2 + v3
    return result

hab = 0


hab = test28.para2_fucn(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==>%d"%hab)
hab = para3_fucn(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==>%d"%hab)