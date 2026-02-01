import pygame

#setup pygame window
pygame.init()
screen = pygame.display.set_mode((500, 500))

while True:
    #check the event type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit the program.
            quit()
    
    #draw rectangle
    pygame.draw.rect(screen, (200,10,130), pygame.Rect(30,30, 60,60))

    pygame.display.flip()