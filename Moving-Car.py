from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def drawCircle(r=0.1, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.001):
        glColor3f(0, 1, 0)

        x = r * cos(theta)
        y = r * sin(theta)

        glVertex(x + xc, y + yc)
    glEnd()

def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(1, 1, 1)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(1, 1,1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()

def draw_road():
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex(10, 2, 0)
    glVertex(10, -5, 0)
    glVertex(-50, -5, 0)
    glVertex(-50, 2, 0)
    glEnd()

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(00.4, 0.4, 0.8, 1)


angle = 0
x = 0
forward = True


def draw():
    global angle
    global x
    global forward

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    #draw_XYZ()


    draw_road()
    drawCircle(1.5, 5.5, 5.8)
    drawCircle(1.4, -0.2, 5.8)
    drawCircle(1.3, -5.9, 5.7)
    drawCircle(1.2, -11.65, 5.5)

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(10, 0, 0)
    glVertex(10, 0, -0.5)
    glVertex(5, 0, -0.5)
    glVertex(5, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.2, 0)
    glVertex(4, 3, -4)
    glVertex(5, 3, -4)
    glVertex(5, -1, -4)
    glVertex(4, -1, -4)
    glEnd()

    glLoadIdentity()


    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.2, 0)
    glVertex(-4, 3, -4)
    glVertex(-3, 3, -4)
    glVertex(-3, -1, -4)
    glVertex(-4, -1, -4)
    glEnd()
    glLoadIdentity()


    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.2, 0)
    glVertex(-20, 3, -4)
    glVertex(-19, 3, -4)
    glVertex(-19, -1, -4)
    glVertex(-20, -1, -4)
    glEnd()
    glLoadIdentity()




    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.2, 0)
    glVertex(-12, 3, -4)
    glVertex(-11, 3, -4)
    glVertex(-11, -1, -4)
    glVertex(-12, -1, -4)
    glEnd()
    glLoadIdentity()



    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(3, 0, 0)
    glVertex(3, 0, -0.5)
    glVertex(-2, 0, -0.5)
    glVertex(-2, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-4, 0, 0)
    glVertex(-4, 0, -0.5)
    glVertex(-9, 0, -0.5)
    glVertex(-9, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-11, 0, 0)
    glVertex(-11, 0, -0.5)
    glVertex(-16, 0, -0.5)
    glVertex(-16, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-18, 0, 0)
    glVertex(-18, 0, -0.5)
    glVertex(-23, 0, -0.5)
    glVertex(-23, 0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(10, 0, 2)
    glVertex(10, 0, 1.5)
    glVertex(5, 0, 1.5)
    glVertex(5, 0, 2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(3, 0, 2)
    glVertex(3, 0, 1.5)
    glVertex(-2, 0, 1.5)
    glVertex(-2, 0, 2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-4, 0, 2)
    glVertex(-4, 0, 1.5)
    glVertex(-9, 0, 1.5)
    glVertex(-9, 0, 2)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-11, 0, 2)
    glVertex(-11, 0, 1.5)
    glVertex(-16, 0, 1.5)
    glVertex(-16, 0, 2)
    glEnd()

    glColor3f(0.5, 0.5, 0)
    glLoadIdentity()
    glTranslate(x + 0.5 * 5, -0.5 * 0.25 * 5, - 0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)


    glColor3f(1, 1, 1)
    glLoadIdentity()
    glTranslate(x, 5*0.25, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)


    glColor3f(0.5, 0.5, 0)
    glLoadIdentity()
    glTranslate(x+0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)


    glLoadIdentity()
    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glColor3f(1, 1, 0)
    glLoadIdentity()
    glTranslate(x + 2.4, 0, 0.5)
    glutSolidSphere(0.2, 100, 100)

    glColor3f(1, 1, 0)
    glLoadIdentity()
    glTranslate(x + 2.4, 0, -0.8)
    glutSolidSphere(0.2, 100, 100)


    glColor3f(1, 0, 0)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, -2)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(2)

    glColor3f(1, 1, 1)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, -1)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(2)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(2)

    glutSwapBuffers()

    if forward:
        angle -= 0.1
        x += 0.2
        if x > 5:
            forward = False
    else:
        angle += 0.1
        x -= 0.2
        if x < -5:
            forward = True


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
