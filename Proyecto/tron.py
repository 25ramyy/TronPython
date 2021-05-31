from turtle import *
from square import square
from vector import vector

p1xy = vector(-100, 0) #pos inicial
p1aim = vector(4, 0) #velocidad
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    "Return True si esta adentro de screen."
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)

setup(420, 420, 420, 0) #tamaño pantalla
hideturtle()


draw()
done()


#333 

setup(420, 420, 420, 0) #tamaño pantalla
hideturtle()
tracer(False)
listen()

onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'k')


onkey(lambda: p1aim.desAcelerattion(), 's')
onkey(lambda: p1aim.Acelerattion(), 'w')
onkey(lambda: p2aim.desAcelerattion(), 'm')
onkey(lambda: p2aim.Acelerattion(), 'i')

draw()
done()
