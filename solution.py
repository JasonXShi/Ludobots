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

        # print("fitness", self.fitness)
        os.system("del fitness"+str(self.ID)+".txt")

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
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1.0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1.0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,-.2,1.0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,-.2,1.0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "Torso_LLeg" , parent= "Torso" , child = "LLeg" , type = "revolute", position = [-0.5,0.2,1.0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_RLeg" , parent= "Torso" , child = "RLeg" , type = "revolute", position = [0.5,0.2,1.0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "LLeg_LLLeg" , parent= "LLeg" , child = "LLLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LLLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "RLeg_RRLeg" , parent= "RLeg" , child = "RRLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RRLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        
        # pyrosim.Send_Joint( name = "Torso_TLeg" , parent= "Torso" , child = "TLeg" , type = "revolute", position = [-0.5,0.5,1.0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="TLeg", pos=[-0.5,0,] , size=[1,0.2,0.2])
        # pyrosim.Send_Joint( name = "Torso_JLeg" , parent= "Torso" , child = "JLeg" , type = "revolute", position = [0.5,0.5,1.0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="JLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        # pyrosim.Send_Joint( name = "TLeg_TTLeg" , parent= "TLeg" , child = "TTLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="TTLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        # pyrosim.Send_Joint( name = "JLeg_JJLeg" , parent= "JLeg" , child = "JJLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="JJLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.ID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LLeg")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "RLeg")
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "LLLeg")
        pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "RRLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 18 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 19 , jointName = "RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 20 , jointName = "Torso_LLeg")
        pyrosim.Send_Motor_Neuron( name = 21 , jointName = "Torso_RLeg")
        pyrosim.Send_Motor_Neuron( name = 22 , jointName = "LLeg_LLLeg")
        pyrosim.Send_Motor_Neuron( name = 23 , jointName = "RLeg_RRLeg")
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName =  4, weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = -1.0 )
        # pyrosim.Send_Synapse( sourceNeuronName = 3 , targetNeuronName = 4 , weight = -1.0 )
        for currentRow in range(c.numSensorNeurons): 
            for currentColumn in range(c.numMotorNeurons): 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self):
        row = random.randint(0,c.numSensorNeurons-1)
        col = random.randint(0,c.numMotorNeurons-1)
        self.weights[row][col] = random.random()*2-1
        