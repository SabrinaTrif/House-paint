from os import *
from pygame.locals import *
import argparse
from app import App

class Main:
    
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                    help="display a numer for a maze")
                    
    parser.add_argument("-l", "--layout", action="store_true",
                    help="number for maze")
    args = parser.parse_args()
    answer = args.square
    if answer==1 :
        mat=[ [2, 2, 2, 2, 2],
              [2 ,0, 0, 0, 2],
              [2, 0, 3, 0, 2],
              [2, 0, 0, 'P', 2],
              [2, 2, 2, 2, 2]]
        costM=[[0,2,3,4,5],
               [1,0,1,2,3],
               [1,5,0,9,9],
               [5,4,5,0,5],
               [8,9,4,3,0]]
        theApp = App(5,5,mat,330,330,7,costM)
        theApp.on_execute()
    if answer==2:
        mat=[[2,2,2,2,2,2,2,2],
             [2,0,0,0,0,0,0,2],
             [2,0,3,3,3,2,0,2],
             [2,0,3,3,3,0,0,2],
             [2,0,0,0,2,0,0,2],
             [2,0,2,0,2,0,0,2],
             [2,0,2,0,2,0,'P',2],
             [2,2,2,2,2,2,2,2]]

        costM=[[0,2,2,2,2,2,2,2],
             [2,0,5,2,3,3,1,2],
             [2,1,0,3,3,2,1,2],
             [2,4,3,0,3,5,1,2],
             [7,3,2,1,0,6,1,2],
             [2,6,2,1,2,0,1,2],
             [6,3,2,3,2,5,0,2],
             [2,2,2,3,1,1,8,0]]
       
        theApp = App(8,8,mat,525,525,23,costM)
        theApp.on_execute()
    if answer==3:
        mat=[[2,2,2,2,2,2,2,2,2],
             [2,0,0,0,0,0,0,0,2],
             [2,2,0,3,3,0,0,0,2],
             [2,0,0,0,0,0,0,2,2],
             [2,0,0,3,3,0,0,0,2],
             [2,2,0,3,3,0,2,0,2],
             [2,0,0,0,0,0,0,0,2],
             [2,0,0,0,2,0,2,'P',2],
             [2,2,2,2,2,2,2,2,2]]
        costM=[[0,2,2,2,2,2,2,2,2],
             [2,0,3,2,4,5,9,2,2],
             [2,2,0,2,2,9,9,1,2],
             [2,6,1,0,8,8,9,2,2],
             [2,1,1,2,0,1,1,5,2],
             [2,2,1,1,3,0,2,5,2],
             [2,1,1,8,5,8,0,6,2],
             [2,3,1,3,2,2,2,0,2],
             [2,4,2,3,2,4,2,5,0]]
        theApp = App(9,9,mat,590,590,35,costM)
        theApp.on_execute()