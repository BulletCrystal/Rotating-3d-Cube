import pygame
import numpy as np
import math


# Initialize Pygame
pygame.init()

# Set display flags
# You can use either pygame.OPENGL or pygame.SCALED for the renderer
flags = pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE
# Add pygame.HWSURFACE for hardware surface
# Add pygame.RESIZABLE if you want the window to be resizable

# Set VSync flag
pygame.display.set_mode((800, 600), flags | pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF)

WIDTH = 900
HEIGHT = 500

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('3d Cube Rotation')
clock = pygame.time.Clock()
# Paramétres
background = (200,200,200)
scale = 150
fi = 0


view_matrix = np.matrix(
    [
        [1,0,0],
        [0,1,0]
    ]

                        )



points3D = [[[1],[0],[-math.sqrt(2)/2]],
            [[0],[1],[-math.sqrt(2)/2]],
            [[-1],[0],[-math.sqrt(2)/2]],
            [[0],[-1],[-math.sqrt(2)/2]],
            [[1],[0],[math.sqrt(2)/2]],
            [[0],[1],[math.sqrt(2)/2]],
            [[-1],[0],[math.sqrt(2)/2]],
            [[0],[-1],[math.sqrt(2)/2]]]

rotated_points = []
Lines = []
a = b = c = 0
speed = 1



running = True
while running :
    fi += 0.02

    rotation_matrix_x= np.matrix(
        [
            [1,0,0],
            [0,math.cos(fi),-math.sin(fi)],
            [0,math.sin(fi),math.cos(fi)]
        ])
    rotation_matrix_y= np.matrix(
        [
            [math.cos(fi),0,math.sin(fi)],
            [0,1,0],
            [-math.sin(fi),0,math.cos(fi)]
        ])
    
    window.fill(background)

    for i in points3D:
        rotated_points.append(np.dot(rotation_matrix_x,np.dot(rotation_matrix_y,np.matrix(i))))

    for i in rotated_points :
        j = np.dot(view_matrix,i)
        pygame.draw.circle(window,(0,0,0),(float(j[0]) * scale + WIDTH/2 ,float(j[1])*scale + HEIGHT/2 ),5)
        Lines.append((float(j[0]) * scale + WIDTH/2 ,float(j[1])*scale + HEIGHT/2))

    for i in range(0, len(Lines) - 4):
            pygame.draw.line(window, (0, 0, 0), Lines[i], Lines[(i + 4) % len(Lines)],3)
            pygame.draw.line(window,(0,0,0),Lines[0],Lines[3],3)
            pygame.draw.line(window,(0,0,0),Lines[7],Lines[4],3)
    for i in range(0, len(Lines)//2):
            if i != 3:
                pygame.draw.line(window, (0, 0, 0), Lines[i], Lines[(i + 1) % len(Lines)],3)
    for i in range(len(Lines)//2, len(Lines)):
            if i != 7:
                pygame.draw.line(window, (0, 0, 0), Lines[i], Lines[(i + 1) % len(Lines)],3)
    rotated_points = []
    Lines = []

    pygame.display.flip()
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

