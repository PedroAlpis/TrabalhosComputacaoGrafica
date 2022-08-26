from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


y0 = -1
yn = 1


x0 = -1
xn = 1

n = 70
dx = (xn - x0)/n
dy = (yn - y0)/n

a = 0




def f(x,y):
    z=(x**5)+(y**5)
    return z


def draw():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glTranslate(0, 0, 0)
    glRotatef(-a,1,0,0)
    drawFace()
    
    glPopMatrix()
    glPushMatrix()
    
    glPopMatrix()
    glutSwapBuffers()
    a += 2


def drawFace():
    y = y0
    for _ in range(n):
        x = x0
        
        glBegin(GL_TRIANGLE_STRIP)
        
        for __ in range(n): 

            glColor3fv([.5,.4,.1])

            glVertex3f(x, y, f(x, y))
            glVertex3f(x, y + dy, f(x, y + dy))
            
            x += dx
        
        glEnd()
        
        y += dy



 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(30,timer,1)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(900,900)
glutCreateWindow("Paraboloide Hiperbólico")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,3.)
gluPerspective(55,800.0/600.0,0.3,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(55,timer,1)
glutMainLoop()
