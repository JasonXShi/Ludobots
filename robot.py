import pybullet as p
import pybullet_data
import time
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import numpy
class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")



    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, timeStep):
        for linkName in self.sensors:
            self.sensors[linkName].GetValue(timeStep)
            if(timeStep == 999):
                print(self.sensors[linkName].values)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, timeStep):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                # print(self.motors.keys())
                # print("jointName: ", jointName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName.encode()].Set_Value(self, desiredAngle, self.sensors)
                print(neuronName, jointName, desiredAngle)

    def Think(self):
        self.nn.Update()
        self.nn.Print()


    def Save_Values(self, var):
        numpy.save("data/"+var+".txt", var)