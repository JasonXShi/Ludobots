from solution import SOLUTION
import constants
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")

        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Print(self):
        print(self.parent.fitness, self.child.fitness)

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        # print("parent",self.parent.weights)
        # print("child", self.child.weights)
        # exit()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
        print(self.parent.fitness)
        print(self.child.fitness)
