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
        # self.Create_Body()
        # self.Create_Brain()
        self.Create_Horse_Body()
        self.Create_Horse_Brain()

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


    def Create_Horse_Body(self):
        for _ in range(13):
            self.s.append(random.choice(["Green", "Blue"]))

        pyrosim.Start_URDF("body.urdf")
        
        legHeights = [random.random() * .3 +.2 , random.random() * .3 + .2 , random.random() * .3 + .2 ]
        totalHeight = sum(legHeights)
        width = random.random() + .5
        length = random.random() + .5
        height = random.random() / 3
        pyrosim.Send_Cube(name = '0', pos = [0, 0, totalHeight + height/2], size=[width, length, height], color= self.s[0])
        lwidth = random.random() * .5 
        llength = random.random() * .5 
        pyrosim.Send_Joint(name = '0_10', parent='0', child='10', type="revolute", position=[width/2, length/2, totalHeight + height/2 - height/2], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = '10', pos=[0, 0, -legHeights[0]/2], size=[lwidth, llength, legHeights[0]], color=self.s[1])
        pyrosim.Send_Joint(name = '0_11', parent='0', child='11', type="revolute", position=[-width/2, length/2, totalHeight + height/2 - height/2], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = '11', pos=[0, 0, -legHeights[0]/2], size=[lwidth, llength, legHeights[0]], color=self.s[2])
        pyrosim.Send_Joint(name = '0_12', parent='0', child='12', type="revolute", position=[width/2, -length/2, totalHeight + height/2 - height/2], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = '12', pos=[0, 0, -legHeights[0]/2], size=[lwidth, llength, legHeights[0]], color=self.s[3])
        pyrosim.Send_Joint(name = '0_13', parent='0', child='13', type="revolute", position=[-width/2, -length/2, totalHeight + height/2 - height/2], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = '13', pos=[0, 0, -legHeights[0]/2], size=[lwidth, llength, legHeights[0]], color=self.s[4])
        
        lwidth = random.random() * .5 +.1
        llength = random.random() * .5 +.1
        pyrosim.Send_Joint(name = str(1) + '_' + str(2) + '0', parent=str(1)+'0', child=str(2) + '0', type="revolute", position=[0, 0, -legHeights[0]], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = str(2) + '0', pos=[0, 0, -legHeights[1]/2], size=[lwidth, llength, legHeights[1]], color=self.s[5])
        pyrosim.Send_Joint(name = str(1) + '_' + str(2) + '1', parent=str(1)+'1', child=str(2) + '1', type="revolute", position=[0, 0, -legHeights[0]], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = str(2) + '1', pos=[0, 0, -legHeights[1]/2], size=[lwidth, llength, legHeights[1]], color=self.s[6])
        pyrosim.Send_Joint(name = str(1) + '_' + str(2) + '2', parent=str(1)+'2', child=str(2) + '2', type="revolute", position=[0, 0, -legHeights[0]], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = str(2) + '2', pos=[0, 0, -legHeights[1]/2], size=[lwidth, llength, legHeights[1]], color=self.s[7])
        pyrosim.Send_Joint(name = str(1) + '_' + str(2) + '3', parent=str(1)+'3', child=str(2) + '3', type="revolute", position=[0, 0, -legHeights[0]], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = str(2) + '3', pos=[0, 0, -legHeights[1]/2], size=[lwidth, llength, legHeights[1]], color=self.s[8])
        
        lwidth = random.random() * .5
        llength = random.random() * .5
        pyrosim.Send_Joint(name = str(2) + '_' + str(3) + '0', parent=str(2)+'0', child=str(3) + '0', type="revolute", position=[0, 0, -legHeights[1]], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = str(3) + '0', pos=[0, 0, -legHeights[2]/2], size=[lwidth, llength, legHeights[2]], color=self.s[9])
        pyrosim.Send_Joint(name = str(2) + '_' + str(3) + '1', parent=str(2)+'1', child=str(3) + '1', type="revolute", position=[0, 0, -legHeights[1]], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = str(3) + '1', pos=[0, 0, -legHeights[2]/2], size=[lwidth, llength, legHeights[2]], color=self.s[10])
        pyrosim.Send_Joint(name = str(2) + '_' + str(3) + '2', parent=str(2)+'2', child=str(3) + '2', type="revolute", position=[0, 0, -legHeights[1]], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = str(3) + '2', pos=[0, 0, -legHeights[2]/2], size=[lwidth, llength, legHeights[2]], color=self.s[11])
        pyrosim.Send_Joint(name = str(2) + '_' + str(3) + '3', parent=str(2)+'3', child=str(3) + '3', type="revolute", position=[0, 0, -legHeights[1]], jointAxis="1 0 0")
        pyrosim.Send_Cube(name = str(3) + '3', pos=[0, 0, -legHeights[2]/2], size=[lwidth, llength, legHeights[2]], color=self.s[12])

        pyrosim.End()

    def Create_Horse_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.ID) + ".nndf")
    
        for i in range(3):
            pyrosim.Send_Motor_Neuron(name = -i, jointName=str(i) + '_' + str(i+1) + '0')
            pyrosim.Send_Motor_Neuron(name = -i-10, jointName=str(i) + '_' + str(i+1) + '1')
            pyrosim.Send_Motor_Neuron(name = -i-20, jointName=str(i) + '_' + str(i+1) + '2')
            pyrosim.Send_Motor_Neuron(name = -i-30, jointName=str(i) + '_' + str(i+1) + '3')
            
        for i in range(0, 12):
            if(self.s[i] == "Green"):
                pyrosim.Send_Sensor_Neuron(name = i , linkName = str(int((i)/4) + 1) + str((i) % 4))
                pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=-i, weight=1)
    
        pyrosim.End()