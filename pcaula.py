from OpenGL.GL import *

import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *

# Configurações
WIDTH, HEIGHT = 440, 700

DESLOCA_X = 54
DESLOCA_Y = 27
VELOCIDADE_INIMIGO = 200
VELOCIDADE_PONTOS = 100

DESLOCA_X_INIMIGO = 54 
DESLOCA_Y_INIMIGO = HEIGHT - 133 + (27*5)
DESLOCA_Y_INIMIGO2 = HEIGHT - 133 + (27*6)

DESLOCA_X_INIMIGO2 = 135

# Variável global para o volume da música
volume = 0.5  # Valor inicial

cont = 1
# cont2 = 1
cont_inimigo = 0
cont_inimigo2 = 0

teste = 0

matriz = [
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
]

matriz2 = [
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,0 ,0, 0, 0],
]

x_pos = 0

x_pos_inimigo = 0
y_pos_inimigo = 0

x_pos_inimigo2 = 0
y_pos_inimigo2 = 0


def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

# Top Gear
#def initialize_sound():
#    pygame.mixer.init()
#    pygame.mixer.music.load("music/top_gear.mp3")  # Carregue sua música de fundo
#    pygame.mixer.music.set_volume(volume)  # Defina o volume (0.0 a 1.0)
#    pygame.mixer.music.play()


#def card_sound():
#    pygame.mixer.init()
#    musica1 = pygame.mixer.Sound("music/som_carro.mp3")  # Carregue sua música de fundo
#    musica1.set_volume(0.5)  # Defina o volume (0.0 a 1.0)
#    channel1 = pygame.mixer.Channel(1)
#    channel1.play(musica1)  # Reproduza a música de fundo em loop infinito
    

def timer(_):
    global cont
    cont += 1
    glutPostRedisplay()
    glutTimerFunc(VELOCIDADE_PONTOS, timer, 0)

def draw_text(pos_x, pos_y, text, color=(0, 0, 0)):
    glColor3fv(color)
    glRasterPos2f(pos_x, pos_y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(character))

def reshape(width, height):
	glutReshapeWindow(WIDTH, HEIGHT)


def quadrado(deslocX, deslocY, color = (0, 0, 0)):
    deslocX = deslocX
    deslocY = deslocY
    # estrutura inicial (preto)
    glBegin(GL_QUADS)
    glColor3fv(color)
    glVertex2f((0 + deslocX), 0 + deslocY)
    glVertex2f((25 + deslocX), 0 + deslocY)
    glVertex2f((25 + deslocX), 25 + deslocY)
    glVertex2f((0 + deslocX), 25 + deslocY)
    glEnd()
    # cinza
    glBegin(GL_QUADS)
    glColor3f(0.85, 0.95, 0.85)
    glVertex2f((0 + 4 + deslocX), 0 + deslocY + 4)
    glVertex2f((17 + 4 + deslocX), 0 + deslocY + 4)
    glVertex2f((17 + 4 + deslocX), 17 + deslocY + 4)
    glVertex2f((0 + 4 + deslocX), 17 + deslocY + 4)
    glEnd()
    #preto
    glBegin(GL_QUADS)
    glColor3fv(color)
    glVertex2f((0 + 7 + deslocX), 0 + deslocY + 7)
    glVertex2f((11 + 7 + deslocX), 0 + deslocY + 7)
    glVertex2f((11 + 7 + deslocX), 11 + deslocY + 7)
    glVertex2f((0 + 7 + deslocX), 11 + deslocY + 7)
    glEnd()
    

def carrinho():
    quadrado(DESLOCA_X + 0 + x_pos,0 + DESLOCA_Y) # esquerda
    quadrado(DESLOCA_X + 27 * 2 + x_pos,0 + DESLOCA_Y) # direita
    quadrado(DESLOCA_X + 27 + x_pos, 27 + DESLOCA_Y) # meio + 2 pra não ficar encostado
    quadrado(DESLOCA_X + 27 + x_pos, 27 * 2 + DESLOCA_Y) # meio + 4 pra não ficar encostado
    quadrado(DESLOCA_X + 0 + x_pos, 27 * 2 + DESLOCA_Y) # meio/direita + 4 pra não ficar encostado
    quadrado(DESLOCA_X + 27 * 2 + x_pos, 27 * 2 + DESLOCA_Y) # meio/esquerda + 4 pra não ficar encostado
    quadrado(DESLOCA_X + 27 + x_pos, 27 * 3 + DESLOCA_Y) # meio/cima + 6 pra não ficar encostado

def inimigo():
    quadrado(DESLOCA_X_INIMIGO + 0 + x_pos_inimigo, 27 * 3 + DESLOCA_Y_INIMIGO + y_pos_inimigo)
    quadrado(DESLOCA_X_INIMIGO + 54 + x_pos_inimigo, 27 * 3 + DESLOCA_Y_INIMIGO + y_pos_inimigo)
    quadrado(DESLOCA_X_INIMIGO + 27 + x_pos_inimigo, 27 * 2 + DESLOCA_Y_INIMIGO + y_pos_inimigo) 
    quadrado(DESLOCA_X_INIMIGO + 27 + x_pos_inimigo, 27 + DESLOCA_Y_INIMIGO + y_pos_inimigo)
    quadrado(DESLOCA_X_INIMIGO + 0 + x_pos_inimigo, 27 + DESLOCA_Y_INIMIGO + y_pos_inimigo) 
    quadrado(DESLOCA_X_INIMIGO + 54 + x_pos_inimigo, 27 + DESLOCA_Y_INIMIGO + y_pos_inimigo) 
    quadrado(DESLOCA_X_INIMIGO + 27 + x_pos_inimigo, 0 + DESLOCA_Y_INIMIGO + y_pos_inimigo)

def inimigo2():
    quadrado(DESLOCA_X_INIMIGO2 + 0 + x_pos_inimigo2, 27 * 3 + DESLOCA_Y_INIMIGO2 + y_pos_inimigo2)
    quadrado(DESLOCA_X_INIMIGO2 + 54 + x_pos_inimigo2, 27 * 3 + DESLOCA_Y_INIMIGO2 + y_pos_inimigo2)
    quadrado(DESLOCA_X_INIMIGO2 + 27 + x_pos_inimigo2, 27 * 2 + DESLOCA_Y_INIMIGO2 + y_pos_inimigo2) 
    quadrado(DESLOCA_X_INIMIGO2 + 27 + x_pos_inimigo2, 27 + DESLOCA_Y_INIMIGO2 + y_pos_inimigo2)
    quadrado(DESLOCA_X_INIMIGO2 + 0 + x_pos_inimigo2, 27 + DESLOCA_Y_INIMIGO2 + y_pos_inimigo2) 
    quadrado(DESLOCA_X_INIMIGO2 + 54 + x_pos_inimigo2, 27 + DESLOCA_Y_INIMIGO2 + y_pos_inimigo2) 
    quadrado(DESLOCA_X_INIMIGO2 + 27 + x_pos_inimigo2, 0 + DESLOCA_Y_INIMIGO2 + y_pos_inimigo2)        

def background():
    glClearColor(0.85, 0.95, 0.85, 0)

    
def andar_inimigo():
    global cont_inimigo, cont, y_pos_inimigo, cont_inimigo2, y_pos_inimigo2, teste

    if(cont_inimigo < 29):
        if(cont_inimigo < 26):
            matriz[1][cont_inimigo] = 1
        if(cont_inimigo > 3):
            matriz[1][cont_inimigo - 4] = 0
        cont_inimigo += 1 
    else:
        cont_inimigo = 0
        y_pos_inimigo = 0
    y_pos_inimigo = y_pos_inimigo -27
    
    if(matriz[1][21] == matriz2[1][21] and matriz2[1][21] == 1):
            cont_inimigo = 0
            y_pos_inimigo = 0
            cont = 0
            matriz[1][21] = 0   

            cont_inimigo2 = 0
            y_pos_inimigo2 = 0
            matriz[0][21] = 0
            teste = 0  

def andar_inimigo2():
    global cont_inimigo, cont, y_pos_inimigo, cont_inimigo2, y_pos_inimigo2, teste

    if(teste > 8 and cont_inimigo2 < 29):
        if(cont_inimigo2 < 26):
            matriz[0][cont_inimigo2] = 1
        if(cont_inimigo2 > 3):
            matriz[0][cont_inimigo2 - 4] = 0
        cont_inimigo2 += 1 
    else:
        cont_inimigo2 = 0
        y_pos_inimigo2 = 0
    y_pos_inimigo2 = y_pos_inimigo2 -27
    
    if(matriz[0][21] == matriz2[0][21] and matriz2[0][21] == 1):
            cont_inimigo = 0
            y_pos_inimigo = 0
            cont = 0
            matriz[1][21] = 0   
            cont_inimigo2 = 0
            y_pos_inimigo2 = 0
            matriz[0][21] = 0
            teste = 0   

    teste = teste + 1

def velocidade_inimigo(_):
    andar_inimigo()
    andar_inimigo2()
    glutTimerFunc(VELOCIDADE_INIMIGO, velocidade_inimigo, 0)
    

def mapa():
    for x in range(0, 270, 25+2):
        for y in range(0, 700, 25+2):
            quadrado(x, y, color=(0.7,0.7, 0.7))

# Função para aumentar o volume (Musica Top Gear)
def aumentar_volume():
    global volume
    if volume < 1.0:
        volume += 0.1
        pygame.mixer.music.set_volume(volume)

# Função para diminuir o volume (Musica Top Gear)
def diminuir_volume():
    global volume
    if volume > 0.0:
        volume -= 0.1
        pygame.mixer.music.set_volume(volume)

def draw():
    glClearColor(0.0,0.0,0.0,0.0)
    background()   
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mapa()
    carrinho()
    inimigo()
    inimigo2()

    draw_text(WIDTH - 80, HEIGHT - 50, str(cont))
    glutSwapBuffers()


def key_callback(key, x, y):
    global matriz2, x_pos
    if key == GLUT_KEY_LEFT or key == b'a' and matriz2[1][21] != 1:
        print("esquerda")
        #card_sound()
        matriz2[0][21] = 0
        matriz2[1][21] = 1
        x_pos = 0
    elif key == GLUT_KEY_RIGHT or key == b'd' and matriz2[0][21] != 1:
        #card_sound()
        matriz2[0][21] = 1
        matriz2[1][21] = 0
        print("direita")
        x_pos = 81
    elif key == b'+':
        aumentar_volume()
    elif key == b'-':
        diminuir_volume()
    for i in matriz2:
        print(i)

def idleFunction():
    # Realize alguma ação quando a aplicação está ociosa
    # Por exemplo, atualizar a animação
    glutPostRedisplay() 

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Carrinho")
    
    glOrtho(0, WIDTH, 0, HEIGHT, -50, 1)
    
    glutTimerFunc(VELOCIDADE_PONTOS, timer, 0)  
    glutTimerFunc(VELOCIDADE_INIMIGO, velocidade_inimigo, 0)
    
    glutDisplayFunc(draw)
    glutIdleFunc(idleFunction)
    #initialize_sound()
    glutSpecialFunc(key_callback)
    glutKeyboardFunc(key_callback)

    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()