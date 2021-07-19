# --- Imports --- #

import pygame as pg
from sys import exit
from pygame.locals import *
pg.init()
            
    
# --- App Class --- #

class App():
    """Generates the App, creates variables used by the app, and lastly creates functions for the app to use"""
    def __init__(self):
        """Creates the Apps entities"""

        # --- Startup Variables --- #
        
        import versions
        from os import getcwd
        self.versions = versions
        self.version = versions.versions.current
        self.clock = pg.time.Clock()
        self.FPS = 60
        del versions

        # --- Font Variables --- #

        self.__font_size = 0
        font_sizes = [10,14,18,24,36,48,60]
        self.__len_sizes = len(font_sizes)-1
        self.__font_dict = dict(map(lambda size, num: (num, pg.font.SysFont("Arial", size)), font_sizes, range(len(font_sizes))))
        self.__autofill_int = 0
        self.__scale = 1.0

        # --- Fill Variables --- #
        
        self.title = input("Include the File Extension when typing in name of image!\nImage Name: ")
        self.word = input("Word to Use: ")

        # --- Windows Variables --- #
        
        pg.display.set_caption("AtlasDesigner")
        self.display = pg.display.set_mode((1280,720), DOUBLEBUF)
        self.image = pg.transform.smoothscale(pg.image.load("{}/images/{}".format(getcwd(), self.title)).convert_alpha(),
                                              (int(self.display.get_width()*self.__scale), int(self.display.get_height()*self.__scale)))
        self.overlay = pg.Surface(self.image.get_size())
        self.__images = (self.image, self.overlay)
        del getcwd, font_sizes

    @property
    def font(self):
        return self.__font_dict[self.font_size]

    @property
    def font_size(self):
        return self.__font_size

    @font_size.setter
    def font_size(self, increment):
        
        if 0 <= self.__font_size+increment <= self.__len_sizes:
            self.__font_size += increment
            
    def autofill(self):
        """Fills the screen with the word chosen on startup"""

        self.__images[1].fill((0,0,0))
        x, y = 0,0
        h = self.font.get_height()-(2*self.__font_size)
        while y < self.image.get_height():
            for letter in self.word:
                w = self.font.size(letter)[0]
                self.__images[self.__autofill_int].blit(self.font.render(letter, True, pg.transform.average_color(self.__images[0], (x,y,w,h))), (x,y))
                x +=  w
                if x >= self.image.get_width():
                    y += h
                    x = 0

    def __events(self):
        """Checks for events"""
        
        event = pg.event.poll()
        if event.type == pg.QUIT:
            pg.register_quit(pg.quit())
            exit(0)
        elif event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                pg.register_quit(pg.quit())
                exit(0)
            if event.key == K_EQUALS:
                self.font_size += 1
                self.autofill()
            elif event.key == K_MINUS:
                self.font_size = -1
                self.autofill()
            elif event.key == K_F5:
                self.__autofill_int = not self.__autofill_int
##                if self.__autofill_int:
##            self.__images[1].fill((0,0,0))
                self.autofill()
                    
    def __draw(self):
        """Draws a pygame.Surface to screen"""

##        self.display.fill((0,0,0))
##        if not self.__autofill_int:
##            self.__images[1].fill((0,0,0))
        self.display.blit(self.__images[self.__autofill_int], (0,0))
        pg.display.flip()

    def __main__(self):
        """Events that can happen while the app is running"""
        
        while True:
            self.__events()
            self.__draw() #Draws all pg.Surfaces to the screen
            self.clock.tick(self.FPS) #Keeps loop running at the correct speed (Frame Per Second)
            print(round(self.clock.get_fps()))
            

# --- Application Loop --- #

if __name__ == "__main__":
    App().__main__()
