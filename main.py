import turtle

ninja = turtle.Turtle()
ninja.speed(10)
# 1: 가장 느림, 3: 느림, 6: 보통, 10: 빠름, 0: 가장 빠름

for i in range(180):
    ninja.forward(100)        # 100 픽셀 수 만큼 이동
    ninja.right(30)           # 오른쪽 30°로 회전
    ninja.forward(20)         # 20 픽셀 수 만큼 이동
    ninja.left(60)            # 왼쪽 60°로 회전
    ninja.forward(50)         # 50 픽셀 수 만큼 이동
    ninja.right(30)           # 오른쪽 30°로 회전

    ninja.penup()             # 펜을 올려서 커서의 이동 흔적이 표시x
    ninja.setposition(0, 0)   # 커서를 (0, 0) 좌표로 이동
    ninja.pendown()           # 펜을 내려서 커서의 이동 흔적이 표시

    ninja.right(2)            # 오른쪽 2°로 회전

turtle.done()                 # Output
