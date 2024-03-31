import turtle 
import time
#Screen
main = turtle.Screen()
main.setup(width =800, height =600)
main.bgcolor("black")
main.title('Pong')
main.tracer(0)

#Paddle A 
paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid= 5, stretch_len=1)
paddle_a.speed(0)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B 
paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid= 5, stretch_len=1)
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.color("red")
ball.shape('circle')
ball.speed(0)
ball.goto(0, 0)
ball.penup()

ball.dx = 2
ball.dy = 2

#Movement Function
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)

#Keybinds
main.listen()
main.onkeypress(paddle_a_up, "w")
main.onkeypress(paddle_b_up, "Up")
main.onkeypress(paddle_a_down, "s")
main.onkeypress(paddle_b_down, "Down")

#Point system
point_a = 0
point_b = 0
text = turtle.Turtle()
text.speed(0)
text.penup()
text.ht()
text.color("Red")
text.goto(20, 200)
text.write(f"Point A: {point_a} Point B: {point_b}", align="Center", font=('monocraft', 30,'normal'))

#Mainloop
while True:
    time.sleep(1/60)
    main.update()
    #Ball Movement
    ball.setx(ball.xcor() + ball.dx * 1.5)
    ball.sety(ball.ycor() + ball.dy * 1.5)

    #Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        point_a += 1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        point_b += 1

    #Collision
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1.03

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1.03

    #Paddle edge
    if paddle_a.ycor() > 250:
        paddle_a.goto(-350, 250)

    if paddle_a.ycor() < -250:
        paddle_a.goto(-350, -250)
    
    if paddle_b.ycor() > 250:
        paddle_b.goto(350, 250)

    if paddle_b.ycor() < -250:
        paddle_b.goto(350, -250)
    
    text.undo()
    text.speed(0)
    text.penup()
    text.ht()
    text.color("Red")
    text.goto(30, 200)
    text.write(f"Point A: {point_a} Point B: {point_b}", align="Center", font=('monocraft', 15,'normal'))

    