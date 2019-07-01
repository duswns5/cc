foods = {"떡볶이":"오뎅","짜장면":"단문지","김밥":"라면","양꼬치":"칭따오"}

while (True) :
    myfood = input(str(list(foods.keys())) + "중 좋아하는 음식을 검색하시오 :")
    if myfood in foods :
        print("입력하신 음식은 : <%s>"%myfood)
        print("<%s> 궁합음식은 <%s> 입니다."%(myfood,foods.get(myfood)))
    elif myfood == "끝" :
        print("종료합니다.")
        break
    else:
        print("입력하신 음식은 : <%s>" % myfood)
        print("그런음식은 세상에 없습니다")

