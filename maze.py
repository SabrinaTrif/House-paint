from os import *
from pygame.locals import *
import pygame
import util
from Directions import Directions
import time



class Maze:
    def __init__(self,n,m,mat,z,costM):
       self.M = m
       self.N = n
       self.maze = mat
       self.zero=z
       self.costM=costM
    def draw(self,display_surf,image_surf):
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]==2:
                display_surf.blit(image_surf,( i*66 , j * 66))
        
    def drawP(self,display_surf,image_surf):
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]=='P':
                display_surf.blit(image_surf,( i*66 , j * 66))

    def drawW(self,display_surf,image_surf):
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]==3:
                display_surf.blit(image_surf,( i*66 , j * 66)) 

    def drawY(self,display_surf,image_surf):
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]==1:
                 display_surf.blit(image_surf,( i*66 , j * 66)) 

    def drawR(self,display_surf):
       c=1
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]=='P':
                 if i + 1 < self.N:
                    if self.maze[i+1][j]==0 or self.maze[i+1][j]==1:
                        self.maze[i+1][j]='P'
                        self.maze[i][j]=1
                        self.zero-=1
                        c=0
                        break
           if c==0:
              break
                          
    def drawL(self,display_surf,yellow_surf):
       c=1
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]=='P':
                 if i - 1 >= 0:
                    if self.maze[i-1][j]==0 or self.maze[i-1][j]==1:
                        self.maze[i-1][j]='P'
                        self.maze[i][j]=1
                        self.zero-=1
                        display_surf.blit(yellow_surf,( i*66 , j * 66)) 
                        c=0
                        break
           if c==0:
               break
       

    def drawD(self,display_surf):
       c=1
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]=='P':
                 if j + 1 <= self.M:
                    if self.maze[i][j+1]==0 or self.maze[i][j+1]==1:
                        self.maze[i][j+1]='P'
                        self.maze[i][j]=1
                        self.zero-=1
                        c=0
                        break
           if c==0:
               break
      
    def drawU(self,display_surf):
       c=1
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]=='P':
                 if j - 1 >= 0:
                    if self.maze[i][j-1]==0 or self.maze[i][j-1]==1:
                        self.maze[i][j-1]='P'
                        self.maze[i][j]=1
                        self.zero-=1
                        c=0
                        break
           if c==0:
               break
     
    
               
    def DFS(self, display_surf,image_surf,yellow_surf):
       #the order: down, up, right, left
       sem=0
       class Node:
           def __init__(self, position, parent):
              self.position = position
              self.parent = parent
       start = Node((self.N-2,self.M-2),None)
       front=util.Stack()
       front.push(start)
       dfsPath=[]
       while not front.isEmpty():
           cCell=front.pop()
           (i,j)=cCell.position
           if self.maze[i][j]==0:
               self.zero-=1
               self.maze[i][j]='P'
           self.drawP(display_surf,image_surf)
           self.drawY(display_surf,yellow_surf)
           pygame.display.flip()
           time.sleep(0.5)
           self.maze[i][j]=1
           if sem==0:
               dfsPath.append((i,j))
               sem=1
           else:
               dfsPath.append((j,i))
           if i==1 and j==1:
              return dfsPath
           (i,j)=cCell.position
           neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
           for dir in neighbors:
               (pi,pj)=dir
               if pi>=0 and pi<self.N and pj>=0 and pj<self.N:
                 if self.maze[pi][pj] == 0:
                    nei = Node(dir,cCell)
                    if (nei not in front.list):
                          front.push(nei) 
               
       return None
    
    def getCost(self,path):
        if path == None:
            return -1
        cost = 0
        for i in path:
            (ii,jj)=i
            cost+=self.costM[ii][jj]
        return cost
        

    def uniformCost(self, display_surf,yellow_surf,image_surf):
       start = (self.N-2,self.M-2)
       visited=[]
       q=util.PriorityQueue()
       q.push((start,[start]),0)
       
       while not q.isEmpty():
           element,path=q.pop()
           #cost = self.getCost(path)
           #print(cost)
           #print(element)
           #luam elementul curent si path-ul
           (i,j)=element
           if i==1 and j==1:  #goal state
               self.drawPath(display_surf,yellow_surf,image_surf,path)
               return path
           if element not in visited:
               neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
               for dir in neighbors:
                   (pi,pj)=dir
                   if pi>=0 and pi<self.N and pj>=0 and pj<self.M:
                       if self.maze[pi][pj] ==0 and (pi,pj) not in visited:
                            Npath = path + [(pi,pj)]
                            cost = self.getCost(path)
                            q.push((dir,Npath),cost)   
       return cost

    def getSuccessors(self,state):
        succesori=[]
        i=state[0]
        j=state[1]
        if i+1<self.N:
            if self.maze[i+1][j]==0 or self.maze[i+1][j]==1 :
                succesori.append(((i+1,j),Directions.WEST))
        if i-1>=0:
            if self.maze[i-1][j]==0 or self.maze[i-1][j]==1:
                succesori.append(((i-1,j),Directions.EAST))
        if j+1<self.N:
            if self.maze[i][j+1]==0 or self.maze[i][j+1]==1:
                succesori.append(((i,j+1),Directions.SOUTH))
        if j-1>=0:
            if self.maze[i][j-1]==0 or self.maze[i][j-1]==1:
                succesori.append(((i,j-1),Directions.NORTH))
        return succesori


    def drawGreen(self,display_surf,yellow_surf,image_surf,path):
        for i in path:
            (ii,jj)=i
            self.maze[ii][jj]='P'
            self.drawP(display_surf,image_surf)
            self.drawY(display_surf,yellow_surf)
            pygame.display.flip()
            time.sleep(0.5)
            if(ii!=1 or jj!=1):
               self.maze[ii][jj]=1

    def BFS(self, display_surf,image_surf,yellow_surf):
         p=[]
         tree = util.Queue()
         tree.push(((self.N-2,self.N-2), []))
         p.append((self.N-2,self.N-2))
         visited = []

         while(not tree.isEmpty()):
          (state, path) = tree.pop()
          p.append(state)
          if(state==(1,1)):
            print(p)
            self.drawGreen(display_surf,yellow_surf,image_surf,p)
            break

          successors = self.getSuccessors(state)
          for i in successors:
            if(i[0] not in visited): 
                visited.append(i[0])
                (ii,jj)=i[0]
                #p.append((ii,jj))
                tree.push((i[0], path + [i[1]]))

         return path


    def manhattanDistance(self, x1, x2,y1,y2 ):
        "Returns the Manhattan distance between points xy1 and xy2"
        return abs( x1 - x2 ) + abs( y1 - y2 )
    def euclidianDistance(self, x1, x2,y1,y2 ):
        "Returns the euclidian distance between points xy1 and xy2"
        return (( x1 - x2 )**2 + ( y1 - y2 )**2)**0.5

    def aStar(self, display_surf,yellow_surf,image_surf):
        tree = util.PriorityQueue()
        h=self.manhattanDistance(self.N-2,1,self.N-2,1)
        g=0
        f=g+h
        tree.push(((self.N-2,self.N-2), []), f)

        visited = []
        p=[]
        while(not tree.isEmpty()):
            (state, path) = tree.pop()
            p.append(state)
            if state==(1,1):
                print(p)
                self.drawGreen(display_surf,yellow_surf,image_surf,p)
                break
            successors = self.getSuccessors(state)
            for i in successors:
                if(i[0] not in visited): 
                    visited.append(i[0])
                    h1=self.manhattanDistance(i[0][0],1,i[0][1],1)
                    g1=self.costM[i[0][0]][i[0][1]]
                    f=g1+h1
                    tree.update((i[0], path + [i[1]]), f)

        return path

    def aStar1(self, display_surf,yellow_surf,image_surf):
        tree = util.PriorityQueue()
        h=self.euclidianDistance(self.N-2,1,self.N-2,1)
        g=0
        f=g+h
        tree.push(((self.N-2,self.N-2), []), f)
        p=[]
        visited = []

        while(not tree.isEmpty()):
            (state, path) = tree.pop()
            p.append(state)
            if state==(1,1):
                self.drawGreen(display_surf,yellow_surf,image_surf,p)
                break
            
            successors = self.getSuccessors(state)
            for i in successors:
                if(i[0] not in visited): 
                    visited.append(i[0])
                    h1=self.euclidianDistance(i[0][0],1,i[0][1],1)
                    g1=self.costM[i[0][0]][i[0][1]]
                    f=g1+h1
                    tree.update((i[0], path + [i[1]]), f)

        return path
    
    

    def drawPath(self,display_surf,yellow_surf,image_surf,path):
        cost=self.getCost(path)
        print(cost)
        costPath=[]
        for i in path:
            (ii,jj)=i
            costPath+=[self.costM[ii][jj]]
            self.maze[ii][jj]='P'
            self.drawP(display_surf,image_surf)
            self.drawY(display_surf,yellow_surf)
            pygame.display.flip()
            time.sleep(0.5)
            self.maze[ii][jj]=1
        print(costPath)

        

    def win(self,display_surf):
       c=1
       for i in range (self.N):
           for j in range (self.M):
               if self.maze[i][j]==0:
                   c=0
                   break
           if c==0:
               break 
       if c==1:
          print("Winner")
          return 1
       return 0 