import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import os
import constants as c
import numpy

class SOLUTION:
    def __init__(self, ID):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)*2-1
        self.ID = ID
        self.nextAvailableID = 0

    def Set_ID(self, ID):
        self.ID = ID
        self.nextAvailableID+=1

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Create_Horse_Body(0.6, 1, [2, 1, 0, 0], [3, 2, 2, 2])
        self.Create_Horse_Brain()

        os.system("start /B python simulate.py " + directOrGui + " " + str(self.ID))

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness"+str(self.ID)+".txt"
        while not os.path.isfile(fitnessFile):
            time.sleep(0.1)
        
        try:
            f = open(fitnessFile, "r")
            self.fitness = float(f.read())
            f.close()
        except:
            time.sleep(1)
            f = open(fitnessFile, "r")
            self.fitness = float(f.read())
            f.close()

        os.system("del fitness"+str(self.ID)+".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Make_Chain(self,direction, num_links, tree_name, linksize_x, linksize_y, linksize_z, lower, upper):
        linksize = [random.uniform(lower, upper), random.uniform(lower, upper), random.uniform(lower, upper)]
        prev_sizes = linksize 
        
        if direction == "+x":
            link_name = "XLink"
            joint_p = [linksize_x / 2, linksize_y / 2, 0]
            joint_a = "1 0 0"   
            link_posn = [linksize[0] / 2, 0, 0]
        elif direction == "-x":
            link_name = "MinXLink"
            joint_p = [-0.5 * linksize_x, linksize_y / 2, 0]
            joint_a = "1 0 0"
            link_posn = [-0.5 * linksize[0], 0, 0]
        else:
            link_name = "ZLink"
            joint_p = [0, linksize_y / 2, linksize_z / 2]
            joint_a = "0 0 1"
            link_posn = [0, 0, linksize[2] / 2]
            
        for i in range(num_links):
            if i == 0: 
                parent = tree_name
                y = linksize_y 
                x = linksize_x
            else:
                if direction == "+x":
                    joint_p = [prev_sizes[0], 0, 0]
                elif direction == "-x":
                    joint_p = [-1 * prev_sizes[0], 0, 0]
                elif direction == "+z":
                    joint_p = [0, 0, prev_sizes[2]]

                parent = tree_name + link_name + str(i - 1)

                y = prev_sizes[1]
                x = prev_sizes[0]

            child = tree_name + link_name + str(i)

            pyrosim.Send_Joint(name = parent + "_" + child, parent = parent, child = child, type = "revolute", 
                            position = [joint_p[0], joint_p[1], joint_p[2]], jointAxis = joint_a)

            if bool(random.getrandbits(1)):
                self.linkNames.append(child)
                self.jointNames.append(parent + "_" + child)
                color = "Green"
            else:
                color = "Blue"

            if direction == "+z":
                linksize[0] = min(linksize[0], x)

            pyrosim.Send_Cube(name = child, 
                            pos = [link_posn[0], link_posn[1], link_posn[2]], 
                            size = [linksize[0], min(linksize[1], y), linksize[2]], color = color)

    def Create_Horse_Body(self, lower, upper, lower_chain, upper_chain): 
        self.linkNames = []
        self.jointNames = []
  
        pyrosim.Start_URDF(f"body{self.ID}.urdf")

        num_links = random.randint(lower_chain[0], upper_chain[0])
        linksize_z = numpy.array([random.uniform(lower, upper) for j in range(num_links + 1)])

        prev_x = random.uniform(lower, upper)
        prev_y = random.uniform(lower, upper)

        pyrosim.Send_Cube(name = "Link0", pos = [0, 0, linksize_z[0] / 2], size = [prev_x, prev_y, linksize_z[0]], color="Blue")

        for i in range(1, num_links):   
            linksize_x = random.uniform(lower, upper)
            linksize_y = random.uniform(lower, upper)

            parent = "Link" +  str(i - 1)
            child = "Link" +  str(i)

            if i == 1:
                jp_y = prev_y / 2
                jp_z = numpy.max(linksize_z) / 2
            else:
                jp_y = prev_y
                jp_z = 0
            
            prev_y = linksize_y

            pyrosim.Send_Joint(name = parent + "_" + child, parent = parent, child = child, type = "revolute", position = [0, jp_y, jp_z], jointAxis = "1 0 0")
            
            if bool(random.getrandbits(1)):
                self.linkNames.append(child)
                self.jointNames.append(parent + "_" + child)
                color = "Green"
            else:
                color = "Blue"

            pyrosim.Send_Cube(name = child, pos = [0, linksize_y / 2, 0], size = [linksize_x, linksize_y, linksize_z[i]], color=color)

            self.Make_Chain("+x", random.randint(lower_chain[1], upper_chain[1]), child, linksize_x, linksize_y, linksize_z[i], lower, upper)
            self.Make_Chain("-x", random.randint(lower_chain[2], upper_chain[2]), child, linksize_x, linksize_y, linksize_z[i] , lower, upper)
            self.Make_Chain("+z", random.randint(lower_chain[3], upper_chain[3]), child, linksize_x, linksize_y, linksize_z[i] , lower, upper)
                
        pyrosim.End()

    def Create_Horse_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.ID) + ".nndf")
        for i in range(len(self.linkNames)):
            pyrosim.Send_Sensor_Neuron(name = i, linkName = self.linkNames[i])
        
        for i in range(len(self.linkNames)):
            pyrosim.Send_Motor_Neuron(name = 1+i + len(self.linkNames), jointName = self.jointNames[i])

        self.weights = numpy.array([numpy.array([numpy.random.rand() for _ in range(len(self.jointNames))]) for _ in range(len(self.linkNames))])
        self.weights = (self.weights * 2) - 1

        for i in range(len(self.linkNames)):        
            for j in range(len(self.jointNames)):
                pyrosim.Send_Synapse(sourceNeuronName = i, targetNeuronName = j + len(self.linkNames), weight = self.weights[i][j])
    
        pyrosim.End()


    def Mutate(self, lower, upper, lower_chain, upper_chain): 
        r = random.randint(1, 8)

        if r == 1:
            lower *= 0.5
            upper *= 0.5

        elif r == 2:
            lower *= 1.5
            upper *= 1.5
        
        elif r == 3:
            upper_chain[0] += 1
            lower_chain[0] += 1
       
        elif r == 4:
            upper_chain[3] += 1
            lower_chain[3] += 1

        # elif r == 5:
        #     upper_chain[0] -= 1
        #     lower_chain[0] -= 1

        # elif r == 6:    
        #     upper_chain[3] -= 1
        #     lower_chain[3] -= 1

        # elif r == 7:
        #     upper_chain[1] -= 1
        #     lower_chain[1] -= 1
        
        else:
            upper_chain[2] += 1
            lower_chain[2] += 1
       

        self.Create_Horse_Body(lower, upper, lower_chain, upper_chain)
        self.Create_Horse_Brain()

        return lower, upper, lower_chain, upper_chain