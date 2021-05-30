 def square(x, y, size, color):
     #dibuja un cuadrado en turtle con los parametros xy donde empieza size lado del cuadrado
     #color es el color del cuadrado
    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.end_fill()
