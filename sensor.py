import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim


class SENSOR:

    def __init__(self,linkName):
        self.values = numpy.zeros(1000)
        self.linkName = linkName

    def GetValue(self, timeStep):
            self.values[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)