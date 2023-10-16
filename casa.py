from OpenGL.GL import *
from OpenGL.GLUT import *
import random

# Configurações
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20

def draw_tri():
    glClearColor(0.0,0.0,0.0,0.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(400, 300)
    glVertex2i(500, 300)
    glVertex2i(450, 350)
    glEnd()
    glFlush()

def draw_qua():
    glColor3f(1.0,1.0,0.4)
    glBegin(GL_QUADS)
    glVertex2f(400, 300)
    glVertex2f(400, 200)
    glVertex2f(500, 200)
    glVertex2f(500, 300)
    glEnd()
    
def draw_parede():
    glColor3f(1.0,1.0,0.8)
    glBegin(GL_QUADS)
    glVertex2i(500, 300)
    glVertex2i(500, 200)
    glVertex2i(650, 200)
    glVertex2i(650, 300)
    glEnd()
    
def draw_telhado():
    glColor3f(1.0,0.4,0.3)
    glBegin(GL_QUADS)
    glVertex2i(650, 300)
    glVertex2i(635, 350)
    glVertex2i(450, 350)
    glVertex2i(500, 300)
    glEnd()

def draw_janela():
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2i(550, 225)
    glVertex2i(550, 275)
    glVertex2i(600, 275)
    glVertex2i(600, 225)
    glEnd()
    
def draw_porta():
    glColor3f(1.0,0.5,0.3)
    glBegin(GL_QUADS)
    glVertex2i(435, 200)
    glVertex2i(465, 200)
    glVertex2i(465, 260)
    glVertex2i(435, 260)
    glEnd()

def draw_tronco():
    glColor3f(1.0,0.5,0.3)
    glBegin(GL_QUADS)
    glVertex2i(200, 200)
    glVertex2i(225, 200)
    glVertex2i(225, 300)
    glVertex2i(200, 300)
    glEnd()
    
def draw_copa():
    glColor3f(0.3,1.0,0.3)
    glBegin(GL_TRIANGLES)
    glVertex2i(185, 220)
    glVertex2i(240, 220)
    glVertex2i(213, 400)
    glEnd()

def draw_terreno():
    glColor3f(0.6,1.0,0.6)
    glBegin(GL_QUADS)
    glVertex2i(0, 0)
    glVertex2i(800, 0)
    glVertex2i(800, 200)
    glVertex2i(0, 200)
    glEnd()

def iterate():
    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    draw_tri()
    draw_parede()
    draw_qua()
    draw_telhado()
    draw_porta()
    draw_janela()
    draw_tronco()
    draw_copa()
    draw_terreno()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Snake Game")
    
    glOrtho(0, WIDTH, HEIGHT, 0, -1, 1)
    
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()

if __name__ == "__main__":
    main()