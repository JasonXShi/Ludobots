import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os

class SOLUTION:
    def __init__(self):
        #create a 3x2 matrix of random values
        self.weights = np.random.rand(3,2)
        # print(self.weights)
        # print(self.weights*2-1)

    def Evaluate(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py "+directOrGui)
        fitnessFile = "fitness.txt"
        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        # print("fitness", self.fitness)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        length = 1.0
        width = 1
        height = 1

        x = 2
        y = 2
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()


    def Create_Body(self):
        length = 1.0
        width = 1
        height = 1
        # x = 0.0
        # y = 0.0
        # z = 0.5
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-0.5] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length,width,height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,2)
        col = random.randint(0,1)
        self.weights[row][col] = random.random()*2-1
        