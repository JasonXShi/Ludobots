from solution import SOLUTION
import constants
import copy
import time
import os 

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        snake = SOLUTION(0)
        snake.Start_Simulation("GUI")
        