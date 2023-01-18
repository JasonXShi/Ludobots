import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
       

        self.amplitude = c.amplitude_f
        self.frequency = c.frequency_f
        self.phaseOffset = c.phaseOffset_f
        self.motorValues = numpy.linspace(0, 2*numpy.pi, 1000)
        if self.jointName == b'Torso_BackLeg':
            print("BackLeg")
            self.amplitude = c.amplitude_f
            self.frequency = c.frequency_f/2
            self.phaseOffset = c.phaseOffset_f
        for i in range(1000):
            self.motorValues[i] = self.amplitude * numpy.sin(self.frequency* i/158.5 + self.phaseOffset)

    def Set_Value(self, robot, timeStep, sensors):
        
        pyrosim.Set_Motor_For_Joint(

            bodyIndex = robot.robotId,

            jointName = self.jointName,

            controlMode = p.POSITION_CONTROL,

            targetPosition =  numpy.sin(self.motorValues[timeStep])*numpy.pi/4,

            maxForce = 100)
