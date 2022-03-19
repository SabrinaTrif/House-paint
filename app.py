from os import *
from pygame.locals import *
import pygame
from maze import Maze
import time
from Directions import Directions
from Actions import Actions
class App:
 
    player = 0
 
    def __init__(self,n,m,mat,wid,hei,zero,costM):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.windowWidth = wid
        self.windowHeight = hei
        self.costM=costM
        self.maze = Maze(n,m,mat,zero,costM)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        self._running = True
        img1=pygame.image.load('pensula.png')
        img1=pygame.transform.smoothscale(img1,(60,60))
        img2=pygame.image.load('caramida.png')
        img2=pygame.transform.smoothscale(img2,(60,60))
        img3=pygame.image.load('w.png')
        img3=pygame.transform.smoothscale(img3,(60,60))
        img4=pygame.image.load('green.png')
        img4=pygame.transform.smoothscale(img4,(60,60))
        self._image_surf = img1.convert()
        self._block_surf = img2.convert()
        self._wind_surf = img3.convert()
        self._yellow_surf = img4.convert()
        
        
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render(self):

        self._display_surf.fill((0,0,0))
        self.maze.draw(self._display_surf, self._block_surf)
        self.maze.drawP(self._display_surf,self._image_surf)
        self.maze.drawW(self._display_surf,self._wind_surf)
        self.maze.drawY(self._display_surf,self._yellow_surf)

        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        ct=0
        while (self._running==True):
            pygame.event.pump()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.maze.drawL(self._display_surf,self._yellow_surf)
                        ct=0
                    else:
                        if event.key== pygame.K_ESCAPE:
                           self._running = False
                        else:
                           if event.key == pygame.K_RIGHT:
                              self.maze.drawR(self._display_surf)
                              ct=0
                          
                           else:
                              if event.key == pygame.K_UP:
                                self.maze.drawU(self._display_surf)
                                ct=0
                                
                              else:
                                if event.key == pygame.K_DOWN:
                                  self.maze.drawD(self._display_surf)
                                  ct=0
                                elif event.key == pygame.K_d:
                                    path=self.maze.DFS(self._display_surf,self._image_surf,self._yellow_surf) 
                                    
                                    print(path) 
                                    self._running = False
                                    ct=1
                                elif event.key == pygame.K_c:
                                    path=self.maze.uniformCost(self._display_surf,self._yellow_surf,self._image_surf)
                                    npath=[]
                                    for i in path:
                                       (ii,jj)=i  
                                       npath+=[(jj,ii)]  
                                    print(npath)   
                                    self._running = False 
                                    ct=1
                                elif event.key == pygame.K_b:
                                    path=self.maze.BFS(self._display_surf,self._image_surf,self._yellow_surf) 
                                    if self.maze.maze[1][1]=='P':
                                        self._running = False
                                        print("gasit")
                                    print(path)
                                elif event.key == pygame.K_a:
                                    path=self.maze.aStar(self._display_surf,self._yellow_surf,self._image_surf)
                                    if self.maze.maze[1][1]=='P':
                                        self._running = False
                                        print("gasit")
                                elif event.key == pygame.K_e:
                                    print("here")
                                    path=self.maze.aStar1(self._display_surf,self._yellow_surf,self._image_surf)
                                    if self.maze.maze[1][1]=='P':
                                        self._running = False
                                        print("gasit")

            if(self.maze.win(self._display_surf)):
               self._running = False
               
            if ct==0:
               self.on_loop()
               self.on_render()
        self.on_cleanup()