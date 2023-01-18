import pybullet as p
import pybullet_data
import time
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import numpy
class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

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
        for jointName in self.motors:
            self.motors[jointName].Set_Value(self, timeStep, self.sensors)

    def Save_Values(self, var):
        numpy.save("data/"+var+".txt", var)