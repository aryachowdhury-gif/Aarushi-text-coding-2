import pygame

#setup pygame window
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_width, screen_height = 500, 500
display_surface = pygame.display.set_mode((screen_width, screen_height))
text = pygame.font.Font(None, 36).render("rectangle", True, pygame.Color('white'))
display_surface.blit(text, (100, 250))

while True:
    #check the event type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit the program.
            quit()
    
    #draw rectangle
    pygame.draw.rect(screen, (200,0,130), pygame.Rect(30,30, 60,60))

    pygame.display.flip()