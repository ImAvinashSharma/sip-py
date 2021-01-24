import time
try:
    def d(distance):
        ang=30
        for i in range(0,1):
            if distance <=500:
                while ang>30:
                    if ang >=180 and ang<0:
                        break
                    ang=ang-5
                    print(ang)
            elif distance >=500 and distance <=1900:
                while ang<100:
                    ang=ang+5
                    print(ang)
                    if ang >=180 and ang<0:
                        break
            else:
                while ang<=160:
                    if ang >=180 and ang<0:
                        break
                    ang=ang+5
                    print(ang)
            time.sleep (0.5)
except:
    print("An exception occurred")
d(52)