import pygame
from pygame.locals import *
 
class GameManager:
    def __init__(self, screenWidth = 640, screenHeight = 640):
        self.displaySurface = None
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        pygame.init()
        self.displaySurface = pygame.display.set_mode((self.screenWidth, self.screenHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
 
    def OnEvent(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
 
    def OnExecute(self): 
        while(self.running):
            for event in pygame.event.get():
                self.OnEvent(event)

gameManager = GameManager()
gameManager.OnExecute()