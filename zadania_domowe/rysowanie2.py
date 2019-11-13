import turtle
def filled():
    turtle.fillcolor("yellow")
    turtle.begin_fill()

def empty():
    turtle.end_fill()

def szachownica(n):
   # turtle.speed(0)
    for i in range(n):
        licznik = 0
        while licznik != n:
            turtle.forward(50)
            turtle.left(270)
            turtle.forward(50)
            turtle.left(270)
            turtle.forward(50)
            turtle.left(270)
            turtle.forward(50)
            if licznik != (n-1):
                turtle.up()
                turtle.forward(50)
                turtle.right(90)
                turtle.down()
            else:
                turtle.right(180)
                turtle.forward(50 * (n-1))
                turtle.left(90)
                turtle.forward(50)
                break


            licznik += 1


print(szachownica(3))
turtle.done()
