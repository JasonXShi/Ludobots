import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName


    
    def Set_Value(self, robot, desiredAngle, sensors):
        
        pyrosim.Set_Motor_For_Joint(

            bodyIndex = robot.robotId,

            jointName = self.jointName,

            controlMode = p.POSITION_CONTROL,

            targetPosition =  numpy.sin(desiredAngle)*numpy.pi/4,

            maxForce = 100)
