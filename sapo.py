from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

tamanho_grid = 12
tamanho_celula = 1.0 / tamanho_grid
coluna_central = (tamanho_grid / 2 * tamanho_celula)

posicao_y = 0
posicao_x = coluna_central

posicao_x_i = 0
posicao_y_i = random.randint(2, tamanho_grid - 2) * tamanho_celula

posicao_x_i2 = 0
posicao_y_i2 = random.randint(2, tamanho_grid - 2) * tamanho_celula

posicao_x_i3 = 0
posicao_y_i3 = random.randint(2, tamanho_grid - 2) * tamanho_celula

# print(tamanho_celula)
def desenha_grid():
    glBegin(GL_LINES)
    glColor3f(0.5, 0.5, 0.5)

    # Desenha linhas horizontais
    for i in range(tamanho_grid + 1):
        glVertex2f(0, i * tamanho_celula)
        glVertex2f(1, i * tamanho_celula)

    # Desenha linhas verticais
    for i in range(tamanho_grid + 1):
        glVertex2f(i * tamanho_celula, 0)
        glVertex2f(i * tamanho_celula, 1)

    glEnd()

def desenha_fundo():
    global tamanho_grid, tamanho_celula
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)
    # altura = math.trunc(tamanho_grid / 4) * tamanho_celula
    altura = 2 * tamanho_celula
    # print(altura * tamanho_celula)
    glVertex2f(0, 0)
    glVertex2f(tamanho_grid * tamanho_celula, 0)
    glVertex2f(tamanho_grid * tamanho_celula, altura)
    glVertex2f(0, altura)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)
    # altura = math.trunc(tamanho_grid / 4) * tamanho_celula
    altura = 2 * tamanho_celula
    # print(altura * tamanho_celula)
    glVertex2f(0, (tamanho_grid - 2) * tamanho_celula)
    glVertex2f(tamanho_grid * tamanho_celula, (tamanho_grid - 2) * tamanho_celula)
    glVertex2f(tamanho_grid * tamanho_celula, tamanho_grid  * tamanho_celula)
    glVertex2f(0, tamanho_grid  * tamanho_celula)
    glEnd()

def desenha_sapo():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    glVertex2f(posicao_x, posicao_y)
    glVertex2f(posicao_x + tamanho_celula, posicao_y)
    glVertex2f(posicao_x + tamanho_celula, posicao_y + tamanho_celula)
    glVertex2f(posicao_x, posicao_y + tamanho_celula)
    glEnd()

def desenha_inimigo(x,y):
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2f(x, y)
    glVertex2f(x + tamanho_celula * 2, y)
    glVertex2f(x + tamanho_celula * 2, y + tamanho_celula)
    glVertex2f(x, y + tamanho_celula)
    glEnd()
# def desenha_inimigo():
#     global posicao_x_i, posicao_y_i
#     glBegin(GL_QUADS)
#     glColor3f(1, 0, 0)
#     glVertex2f(posicao_x_i, posicao_y_i)
#     glVertex2f(posicao_x_i + tamanho_celula * 2, posicao_y_i)
#     glVertex2f(posicao_x_i + tamanho_celula * 2, posicao_y_i + tamanho_celula)
#     glVertex2f(posicao_x_i, posicao_y_i + tamanho_celula)
#     glEnd()

def colisao(obj,mov,x,y):
    global tamanho_celula, posicao_x_i, posicao_y_i, posicao_x_i2, posicao_y_i2, posicao_x_i3, posicao_y_i3
    if obj == 'sapo':
        if round(x,2) <= 0 and mov == 'a':
            return True
        if round(x + tamanho_celula,2) >= round(tamanho_grid * tamanho_celula,2) and mov == 'd':
            return True
        if round(y + tamanho_celula,2) <= round(tamanho_celula,2) and mov == 's':
            return True
        if round(y + tamanho_celula,2) >= round(tamanho_grid * tamanho_celula,2) and mov == 'w':
            return True
        if mov == 'inimigo':
            if (round(x,2) < round(posicao_x_i,2) + round(2 * tamanho_celula,2) and
                round(x,2) + round(tamanho_celula,2) > round(posicao_x_i,2) and
                round(y,2) < round(posicao_y_i,2) + round(tamanho_celula,2) and
                round(y,2) + round(tamanho_celula,2) > round(posicao_y_i,2)):
                return True
            if (round(x,2) < round(posicao_x_i2,2) + round(2 * tamanho_celula,2) and
                round(x,2) + round(tamanho_celula,2) > round(posicao_x_i2,2) and
                round(y,2) < round(posicao_y_i2,2) + round(tamanho_celula,2) and
                round(y,2) + round(tamanho_celula,2) > round(posicao_y_i2,2)):
                return True
            if (round(x,2) < round(posicao_x_i3,2) + round(2 * tamanho_celula,2) and
                round(x,2) + round(tamanho_celula,2) > round(posicao_x_i3,2) and
                round(y,2) < round(posicao_y_i3,2) + round(tamanho_celula,2) and
                round(y,2) + round(tamanho_celula,2) > round(posicao_y_i3,2)):
                return True
        else:
            return False
    if obj == 'inimigo':
        if round(x,2) >= round((tamanho_grid * tamanho_celula),2):
            return True

def andar_inimigo(valor):
    global tamanho_celula, posicao_x, posicao_y, posicao_x_i, posicao_y_i, posicao_x_i2, posicao_y_i2, posicao_x_i3, posicao_y_i3

    posicao_x_i += tamanho_celula
    posicao_x_i2 += tamanho_celula
    posicao_x_i3 += tamanho_celula

    glutPostRedisplay()
    glutTimerFunc(500, andar_inimigo, 0)
    if (colisao('sapo','inimigo', posicao_x, posicao_y)) == True:
        posicao_x = coluna_central
        posicao_y = 0

    if (colisao('inimigo','', posicao_x_i, None)) == True:
        posicao_x_i = 0
        posicao_y_i = random.randint(2, (tamanho_grid - 2)) * tamanho_celula
    if (colisao('inimigo','', posicao_x_i2, None)) == True:
        posicao_x_i2 = 0
        posicao_y_i2 = random.randint(2, (tamanho_grid - 2)) * tamanho_celula
    if (colisao('inimigo','', posicao_x_i3, None)) == True:
        posicao_x_i3 = 0
        posicao_y_i3 = random.randint(2, (tamanho_grid - 2)) * tamanho_celula

def andar_inimigo2(valor):
    global tamanho_celula, posicao_x_i2, posicao_y_i2, posicao_x, posicao_y

    posicao_x_i2 += tamanho_celula

    glutPostRedisplay()
    glutTimerFunc(450, andar_inimigo2, 0)
    if (colisao('sapo','inimigo', posicao_x, posicao_y)) == True:
        posicao_x = coluna_central
        posicao_y = 0

    if (colisao('inimigo','', posicao_x_i2, None)) == True:
        posicao_x_i2 = 0
        posicao_y_i2 = random.randint(2, (tamanho_grid - 2)) * tamanho_celula


def andar_inimigo3(valor):
    global tamanho_celula, posicao_x_i3, posicao_y_i3, posicao_x, posicao_y

    posicao_x_i3 += tamanho_celula

    glutPostRedisplay()
    glutTimerFunc(400, andar_inimigo3, 0)
    if (colisao('sapo','inimigo', posicao_x, posicao_y)) == True:
        posicao_x = coluna_central
        posicao_y = 0

    if (colisao('inimigo','', posicao_x_i3, None)) == True:
        posicao_x_i3 = 0
        posicao_y_i3 = random.randint(2, (tamanho_grid - 2)) * tamanho_celula

def keyboard(key, x, y):
    global posicao_x, posicao_y, coluna_central

    if key == b'w':
        if(colisao('sapo','w', posicao_x, posicao_y)) == False:
            posicao_y += tamanho_celula
    elif key == b's':
        if(colisao('sapo','s', posicao_x, posicao_y)) == False:
            posicao_y -= tamanho_celula
    elif key == b'a':
        if (colisao('sapo','a', posicao_x, posicao_y)) == False:
            posicao_x -= tamanho_celula
    elif key == b'd':
        if (colisao('sapo','d', posicao_x, posicao_y)) == False:
            posicao_x += tamanho_celula

    if (colisao('sapo','inimigo', posicao_x, posicao_y)) == True:
        posicao_x = coluna_central
        posicao_y = 0
    glutPostRedisplay()

def display():
    global posicao_x_i, posicao_x_i2, posicao_x_i3, posicao_y_i, posicao_y_i2, posicao_y_i3
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    gluOrtho2D(0, 1, 0, 1)

    desenha_fundo()
    desenha_grid()
    desenha_sapo()
    desenha_inimigo(posicao_x_i, posicao_y_i)
    desenha_inimigo(posicao_x_i2, posicao_y_i2)
    desenha_inimigo(posicao_x_i3, posicao_y_i3)

    glFlush()

def main():
    glutInit()
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Jogo Sapo")
    glutTimerFunc(10, andar_inimigo, 0)
    glutTimerFunc(10, andar_inimigo2, 0)
    glutTimerFunc(10, andar_inimigo3, 0)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()