import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import os
import constants as c

class SOLUTION:
    def __init__(self, ID):
        #create a 3x2 matrix of random values
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)*2-1
        self.ID = ID
        self.nextAvailableID = 0
        self.s = []
        # print(self.weights)
        # print(self.weights*2-1)

    def Set_ID(self, ID):
        self.ID = ID
        self.nextAvailableID+=1

    def Evaluate(self, directOrGui):
        # self.Create_World()
        # self.Create_Body()
        # self.Create_Brain()
        # os.system("start /B python simulate.py " + directOrGui + " " + str(self.ID))
        # fitnessFile = "fitness"+str(self.ID)+".txt"
        # while not os.path.isfile(fitnessFile):
        #     time.sleep(0.1)
        # f = open(fitnessFile, "r")
        # self.fitness = float(f.read())
        # f.close()
        # print("fitness", self.fitness)
        pass

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + directOrGui + " " + str(self.ID))

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness"+str(self.ID)+".txt"
        while not os.path.isfile(fitnessFile):
            time.sleep(0.1)
        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        f.close()

        os.system("del fitness"+str(self.ID)+".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        length = random.random() + 0.25
        width = random.random() + 0.25
        height = random.random() + 0.25
        
        self.s.append(random.choice(["Green", "Blue"]))
        pyrosim.Send_Cube(name="0", pos=[0, width/2, height/2 ] , size=[length, width, height], color = self.s[0])

        pHeight = height
        pWidth = width
        for i in range(1, random.randint(5,10)):
            if i == 1:
                pJointHeight = 0
                h = min(height/2, pHeight/2)
            else:
                h = min(height/2, pHeight/2) - pJointHeight
            length = random.random() + 0.25
            width = random.random() + 0.25
            height = random.random() + 0.25

            pyrosim.Send_Joint(name = str(i-1) + '_' + str(i) , parent= str(i-1) , child = str(i), 
                                position = [0, pWidth, h], jointAxis="0 0 1", type = "revolute")

            pWidth = width
            pHeight = height
            pJointHeight = h + pJointHeight

            self.s.append(random.choice(["Green", "Blue"]))
            pyrosim.Send_Cube(name=str(i), pos=[0, width / 2, height/2 -pJointHeight] , size=[length,width,height], color=self.s[i])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.ID)+".nndf")

        for i in range(len(self.s) - 1):
            pyrosim.Send_Motor_Neuron(name = str(-i), jointName = str(i) + '_' + str(i+1))

        for i in range(len(self.s)):
            if(self.s[i] == "Green"):
                s = str(i)
                pyrosim.Send_Sensor_Neuron(name = s , linkName = s)

