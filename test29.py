class Car:
    #자동차의 필드
    color = ""
    speed = 0

    #자동차의 메서드
    def __init__(self):
        self.color = "노랑"
        self.speed = 50
    def upspeed(self,value) :
        #현재 속도에서 증가할_속도량만큼 속도를 올리는 코드
        self.speed+=value
    def downSpeed(self,value):
        #현재 속도에서 감소할_속도량만큼 속도를 내리는 코드
        self.speed-=Value
