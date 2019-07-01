#  ss = "파이썬최고"
#  print(ss[0])
#  print(ss[1:3])
#  print(ss[3:])
#
#  s1 = ss.replace("파이썬","클라우드")
#  print(s1)
#
#  ss = "살려주세요"
#  print(len(ss))
#
# ss = " 달려라 하니 "
# print(">"+ ss.strip() + "<")

# ss = "Python을 열심히 공부중"
# ss.strip()
# ss = "하나:둘:셋"
# ss.strip(":")


# ss = """떠나는 그대여 울지말아요 슬퍼말아요 내가 단념할게요 마음편히 가시도록 내사랑 그대가 날 떠나 행복 할수있다면 내가 떠나갈게요 그대 만나 느낀 기억도
# 내가 가진 행복도 모두 가져가세요 남은 그대 삶의 축복을"""
#
# print(len(ss))

import operator

inStr = """내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다. 내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다.
        내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞은 누가 나의 이름을 불러다오. 그에게로 가서 나도 그의 꽃이 되고 싶다.
        우리들은 모두 무엇이 되고 싶다. 
        나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다."""

countDic = {}
countList = []

if __name__ == "__main__" :
    for ch in inStr :

        if "가" <= ch and ch <= "힣" :
            if ch in countDic:
                countDic[ch] = countDic[ch] + 1
            else:
                countDic[ch] = 1

    countList = sorted(countDic.items(),key = operator.itemgetter(1),reverse = True )

    print("원문\n",inStr)
    print("----------------------")
    print("문자\t빈도수")
    print("----------------------")
    print(countList)
    for i in range(0,len(countList)) :
        print(countList[i][0],"\t",countList[i][1])