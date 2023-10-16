# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    paramW = 0.0
    
    glTranslatef(paramW,0.0, -5)
    
    
    while True:
        for i in range(500):
            print(i)
            if i < 250:
                gluPerspective(i, (display[0]/display[1]), 0.1, 50.0)
            else:
                gluPerspective(i-250, (display[0]/display[1]), 0.1, 50.0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        paramW = paramW + 0.001
                    elif event.key == pygame.K_s:
                        print("S")
                    elif event.key == pygame.K_a:
                        print("A")
                    elif event.key == pygame.K_d:
                        print("D")
                        
            glRotatef(1, 3, 1, 1)
            glTranslatef(paramW,0.0, 0.0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            Cube()
            pygame.display.flip()
            pygame.time.wait(10)


main()