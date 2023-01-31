from solution import SOLUTION
import constants
import copy
import time
import os 

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(constants.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Evolve(self):
        self.Evaluate(self.parents)
        

        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
    def Show_Best(self):
        bestParent = self.parents[0]
        for i in range(len(self.parents)):
            if self.parents[i].fitness < bestParent.fitness:
                bestParent = self.parents[i]
        bestParent.Start_Simulation("GUI")
        print(bestParent.fitness)
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        

    def Print(self):
        print()
        for i in range(len(self.parents)):
            print(self.parents[i].fitness, self.children[i].fitness)
        print()

    def Spawn(self):
        self.children  = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
        
    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()

    def Select(self):
        for i in range(len(self.parents)):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT")
            # time.sleep(5)
        
        for i in range(len(solutions)):
            solutions[i].Wait_For_Simulation_To_End()