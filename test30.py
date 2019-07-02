import io
import sys
from test29 import  Car
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

myCar = Car()

myCar.color = "Red"
myCar.speed = 20

myCar.upspeed(40)
myCar.downSpeed(10)


print("자동차의 색상은 %s이며 속도는 %d입니다."%(myCar.color,myCar.speed))
