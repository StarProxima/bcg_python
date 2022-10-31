import math
import pygame as pygame
import random as random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
verticies = (
    (0.1, -0.1, -0.1),
    (0.1, 0.1, -0.1),
    (-0.1, 0.1, -0.1),
    (-0.1, -0.1, -0.1),
    (0.1, -0.1, 0.1),
    (0.1, 0.1, 0.1),
    (-0.1, -0.1, 0.1),
    (-0.1, 0.1, 0.1)
)
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

verticies2 = (
    (-0.8, -1, -1),
    (-0.8, -0.8, -1),
    (-1, -0.8, -1),
    (-1, -1, -1),
    (-0.8, -1, -0.8),
    (-0.8, -0.8, -0.8),
    (-1, -1, -0.8),
    (-1, -0.8, -0.8)
)

verticies3 = (
    (0.8,  1,  1),
    (0.8,  0.8,  1),
    (1,  0.8,  1),
    (1,  1,  1),
    (0.8,  1,  0.8),
    (0.8,  0.8,  0.8),
    (1,  1,  0.8),
    (1,  0.8,  0.8)
)


def Cube():
    glRotatef(1, 3, 1, 1)
    xr = random.randint(-100, 100)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()
    glRotatef(1, 1, xr, 1)
    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies2[vertex])
    glEnd()
    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies3[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1200, 800)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    screen.fill((1, 1, 1))
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glClearColor(1, 1, 1, 1)
    grad = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_QUADS)
        glColor3f(0.86, 0.14, 0.12)
        glVertex2f(-2, 1.0)
        glVertex2f(2, 1.0)
        glVertex2f(2, -1.0)
        glVertex2f(-2, -1.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(1, 0.78, 0.15)
        glVertex2f(-2, 1)
        glVertex2f(0, 0)
        glVertex2f(-2, -1.0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(0, 0, 0)
        glVertex2f(-2, 1)
        glVertex2f(-0.66, 0)
        glVertex2f(-2, -1.0)
        glEnd()
        glTranslated(0.0001, 0.0, 0.0)
        glBegin(GL_TRIANGLES)

        glColor3f(1, 1, 1)

        R = 0.25

        grad += 0.5

        xA = R * math.cos((grad + 90) * math.pi / 180)
        yA = R * math.sin((grad + 90) * math.pi / 180)
        xB = R * math.cos((grad + 306) * math.pi / 180)
        yB = R * math.sin((grad + 306) * math.pi / 180)
        xC = R * math.cos((grad + 162) * math.pi / 180)
        yC = R * math.sin((grad + 162) * math.pi / 180)
        xD = R * math.cos((grad + 18) * math.pi / 180)
        yD = R * math.sin((grad + 18) * math.pi / 180)
        xE = R * math.cos((grad + 234) * math.pi / 180)
        yE = R * math.sin((grad + 234) * math.pi / 180)

        xA2 = (R/2.3) * math.cos((grad + 90 + 33.75) * math.pi / 180)
        yA2 = (R/2.3) * math.sin((grad + 90 + 33.75) * math.pi / 180)
        xB2 = (R/2.3) * math.cos((grad + 306+33.75) * math.pi / 180)
        yB2 = (R/2.3) * math.sin((grad + 306+33.75) * math.pi / 180)
        xC2 = (R/2.3) * math.cos((grad + 162+33.75) * math.pi / 180)
        yC2 = (R/2.3) * math.sin((grad + 162+33.75) * math.pi / 180)
        xD2 = (R/2.3) * math.cos((grad + 18 + 33.75) * math.pi / 180)
        yD2 = (R/2.3) * math.sin((grad + 18 + 33.75) * math.pi / 180)
        xE2 = (R/2.3) * math.cos((grad + 234+33.75) * math.pi / 180)
        yE2 = (R/2.3) * math.sin((grad + 234+33.75) * math.pi / 180)

        # glVertex2f(xA, xA)
        # glVertex2f(xA2, xA2)a

        x = -1.4

        glVertex2f(xA + x, yA)
        glVertex2f(xE + x, yE)
        glVertex2f(xB2 + x, yB2)

        glVertex2f(xC + x, yC)
        glVertex2f(xE2 + x, yE2)
        glVertex2f(xD + x, yD)

        glVertex2f(xA + x, yA)
        glVertex2f(xB + x, yB)
        glVertex2f(xC2 + x, yC2)

        glEnd()

        pygame.display.flip()
        pygame.time.wait(1)


main()
