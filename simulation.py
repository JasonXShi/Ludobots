from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
class SIMULATION:
    def __init__(self, arg, solutionID):
        self.directOrGui = arg
        if arg == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif arg == "GUI":
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        else:
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.stepSimulation()
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT(solutionID)
        self.world = WORLD()

    def Run(self):
        for i in range(400):
            # print(i)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGui == "GUI":
                time.sleep(1./60.)

        # numpy.save("data/backLegSensorValues.txt", backLegSensorValues)
        # numpy.save("data/frontLegSensorValues.txt", frontLegSensorValues)
        # numpy.save("data/targetAngles_f.txt", targetAngles_f)
        # numpy.save("data/targetAngles_b.txt", targetAngles_b)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        return self.robot.Get_Fitness()