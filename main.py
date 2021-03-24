
import ctypes
import os

pygame.init()
pygame.font.init()
width = 700
height = 600


"""ctypes.windll.user32.SetProcessDPIAware()
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
gameDisplay = pygame.display.set_mode(true_res,pygame.FULLSCREEN)"""


simulation_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Smart lyskryss')

clock = pygame.time.Clock()
crashed = False




time = pygame.time.get_ticks()



while not crashed:

    

    

    for event in pygame.event.get():

        

        if event.type == pygame.QUIT:
            crashed = True
    

    clock.tick(60)
pygame.quit()
quit()