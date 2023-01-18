from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.stepSimulation()
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT()
        self.world = WORLD()
        

    def Run(self):
        for i in range(1000):
            print(i)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(1./60.)

        # numpy.save("data/backLegSensorValues.txt", backLegSensorValues)
        # numpy.save("data/frontLegSensorValues.txt", frontLegSensorValues)
        # numpy.save("data/targetAngles_f.txt", targetAngles_f)
        # numpy.save("data/targetAngles_b.txt", targetAngles_b)

    def __del__(self):
        p.disconnect()