from turtle import *
def havaifisek():
   
     pensize(2)
     speed(4)
     color("blue")
     for i in range(36):
          forward(100)
          backward(100)
          left(10)
     
     color("yellow")
     setpos(100,100)
     for i in range(36):
          forward(100)
          backward(100)
          left(10)
     
     color("blue")
     goto(-100,100)
     for i in range(36):
          forward(100)
          backward(100)
          left(10)
     
     color("yellow")
     goto(-100,-100)
     for i in range(36):
          forward(100)
          backward(100)
          left(10)
     
     color("blue")
     goto(100,-100)
     for i in range(36):
          forward(100)
          backward(100)
          left(10)
     done()
havaifisek()