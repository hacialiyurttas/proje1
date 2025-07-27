def kablumbaga():
    import random
    import turtle

    pencere=turtle.Screen()
    pencere.setup(900,400)
    pencere.title("Kaplumbağa Yarışı")
    pencere.bgcolor("lightgray")

    k1=turtle.Turtle()
    k1.shape("turtle")
    k1.color("green")
    k1.penup()
    k1.goto(-350,100)

    k2=k1.clone()
    k2.color("blue")
    k2.penup()
    k2.goto(-350,-100)

    k1.goto(300,60)
    k1.pendown()
    k1.circle(40)
    k1.penup()
    k1.goto(-350,100)

    k2.goto(300,-140)
    k2.pendown()
    k2.circle(40)
    k2.penup()
    k2.goto(-350,-100)

    def yeniOyun():
        k1.goto(-350, 100)
        k2.goto(-350, -100)
    def zarAt():
        if k1.xcor() >= 270:
            print("Yeşil kazandı.")
        elif k2.xcor()>=270:
            print("Mavi kazandı.")
        else:
            global zar1
            zar1=random.randint(1,6)
            k1.fd(zar1)

    def zarAt2():
        if k1.xcor() >= 270:
            print("Yeşil kazandı.")
            exit   
        elif k2.xcor()>=270:
            print("Mavi kazandı.")
            exit
        else:

            zar2=random.randint(1,6)
            k2.fd(zar2)


    pencere.listen()
    pencere.onkey(zarAt,"Right")
    pencere.onkey(zarAt2,"space")
    pencere.onkey(yeniOyun,"y")
    pencere.onkey(turtle.bye,"Escape")
    screen=turtle.Screen()
    screen.exitonclick()
kablumbaga()