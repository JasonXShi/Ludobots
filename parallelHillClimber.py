from solution import SOLUTION
import constants
import copy
import time
import os 
import numpy
import matplotlib.pyplot as plt


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.fitness_arr = []
        # os.system("del brain*.nndf")
        # os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(constants.populationSize):
            print("Creating Parent: ", i)
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Evolve(self):
        self.Evaluate(self.parents)
        

        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()

        plt.plot(self.fitness_arr)
        plt.ylabel('Distance from center')
        plt.show()
        
    def Show_Best(self):
        bestParent = self.parents[0]
        for i in range(len(self.parents)):
            if self.parents[i].fitness > bestParent.fitness:
                bestParent = self.parents[i]
        bestParent.Start_Simulation("GUI")
        print("best fitness", bestParent.fitness)
        

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
        lower, upper, lower_chain, upper_chain = 0.5, 1, [3, 1, 0, 0], [5, 1, 1, 1]

        for i in self.children: 
            lower, upper, lower_chain, upper_chain = self.children[i].Mutate(lower, upper, lower_chain, upper_chain)

    def Select(self):
        curr_fitness_arr = numpy.zeros((len(self.parents)))

        for i in range(len(self.parents)):
            if self.parents[i].fitness < self.children[i].fitness:
                self.parents[i] = self.children[i]
                curr_fitness_arr = numpy.append(curr_fitness_arr, self.parents[i].fitness)

        self.fitness_arr = numpy.append(self.fitness_arr, curr_fitness_arr)

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT")
            # time.sleep(5)
        
        for i in range(len(solutions)):
            solutions[i].Wait_For_Simulation_To_End()
