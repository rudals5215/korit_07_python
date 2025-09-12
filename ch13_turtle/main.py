from turtle import Turtle, Screen
from random import Random
# turtle 모듈에서 Turtle, Screen 클래스를 import 해왔습니다.

t = Turtle()        # 터틀 객체를 생성했고, 객체명 t
screen = Screen()   # 스크린 객체 생성
# 이상의 경우만 작성했을 때 모니터가 깜빡이는 것을 확인할 수 있는데, 이는 코드가 다 돌아가면 프로그램이 종료되기 때문에, 창이 켜졌다가 꺼지는 것입니다.

t.shape('turtle')               # Turtle의 메서드를 호출했는데 argument가 str
t.color('white')
screen.bgcolor('black')

# 랜덤 객체 생성
random = Random()
colors = [
    'dark red',
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
    'light yellow',
]


# t.forward(100.4)
# t.penup()
# t.forward(100.4)
# t.pendown()
# t.forward(100.4)
# t.forward(30.4)

# 점선 그리는 반복문
# for turtle in range(10):
#     t.forward(20)
#     t.penup()
#     t.forward(20)
#     t.pendown()
#
# t.left(90)

# for _ in range(4) :
#     for turtle in range(10):
#         t.forward(20)
#         t.penup()
#         t.forward(20)
#         t.pendown()
#     t.left(90)

# for _ in range(4):
#     t.forward(100)
#     t.left(90)
#
# for _ in range(3):
#     t.forward(100)
#     t.left(120)
#
# for _ in range(5):
#     t.forward(100)
#     t.left(72)
#
# for _ in range(6):
#     t.forward(100)
#     t.left(60)
#
# for _ in range (8):
#     t.forward(100)
#     t.left(45)

'''
이상을 일반화 시키기 위해서 알 수 있는것은
삼각형일 때 120
사각형일 때 90
오각형일 떄 60
육각형일 때 60
...
십각형일 때 36
'''
# n = int(input('몇각형을 생성할까요 >>> '))
# for i in range(n):
#     t.forward(100)
#     t.left(360/n)



# for i in range(3,11):
#     for _ in range(i):
#         t.forward(100)
#         t.left(360/i)
#     t.color(random.choice(colors))

# n = int(input('몇각형까지 생성할까요 >>> '))
# for i in range(3,n+1):
#     for j in range(i):
#         t.forward(100)
#         t.left(360/i)
#         t.color(random.choice(colors))

# def draw_shape(n) :
#     for _ in range(n):
#         t.forward(100)
#         t.left(360/n)
#         t.color(random.choice(colors))
#
# for i in range(3,11):
#     draw_shape(i)
#
# def draw_dotted_line() :
#     for _ in range(10) :
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         t.pendown()
#
# def draw_dotted_shape(n):
#     for _ in range(n) :
#         draw_dotted_line()
#         t.left(360/n)
#     t.color(random.choice(colors))
#
# for i in range(3,11) :
#     draw_dotted_shape(i)

# t.forward(100)
# print(t.heading())
# t.left(90)
# t.forward(100)
# print(t.heading())
# t.left(30)
# t.forward(100)
# print(t.heading())
# t.right(30)
# t.forward(100)
# print(t.heading())
# t.setheading(30)
# t.forward(100)
# print(t.heading())

# .heading()의 return 값은 float
# .setheading()의 parameter가 float / return None

# t.setheading(t.heading()+100)

# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)

# t.color(random.choice(colors))
# t.circle(100)
# # 거북이 머리 다른쪽으로 돌려서 다음 원이 겹치지 않게끔 하는 함수
# t.setheading(t.heading() + 10)

# for _ in range(36) :
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 10)
#
# for _ in range(10) :
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 36)

# 함수화를 위한 일반식을 main에 작성하겠습니다.
# n = int(input('몇개의 원을 그리겠습니까? >>> '))
# for _ in range(n):
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + (360/n))
t.speed(0)
# 함수화를 시키겠습니다.
def draw_spirograph(size_of_gap):
    for _ in range(size_of_gap):
        t.color(random.choice(colors))
        t.circle(100)
        t.setheading(t.heading() + (360 / size_of_gap))
#
# draw_spirograph(360)
# 이상의 코드에서의 문제점은
# 1. 매개변수인 size_of_gap은 n 번째 원과 n+1 번째 원의 각도 차이를 나타내는 것 같은데, 실제로는 반복횟수를 통제하고 있습니다.
# 2. 이상의 상황에서 나타나는 점은 360을 입력했을 때, 제자리에서 원이 생성되는 것이 아니라, 그냥 360번을 반복한다는 점입니다.
draw_spirograph(360)





# t.circle(100)
# t.left(90)
# t.penup()
# t.forward(100)
# t.pendown()
# def draw_shape(n) :
#     for _ in range(n):
#         t.forward(100)
#         t.left(360/n)
#         t.color(random.choice(colors))
#
# for i in range(3,11):
#     draw_shape(i)


screen.exitonclick()
