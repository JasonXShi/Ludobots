import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import math


amplitude_f = numpy.pi/4
frequency_f =  15
phaseOffset_f = 0

amplitude_b = numpy.pi/4
frequency_b =  10
phaseOffset_b = numpy.pi/4

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.stepSimulation()

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAngles_f = numpy.linspace(0, 2*numpy.pi, 1000)
# targetAngles = numpy.sin(targetAngles)

for i in range(1000):
    targetAngles_f[i] = amplitude_f * numpy.sin(frequency_f* i/158.5 + phaseOffset_f)

targetAngles_b = numpy.linspace(0, 2*numpy.pi, 1000)
# targetAngles = numpy.sin(targetAngles)

for i in range(1000):
    targetAngles_b[i] = amplitude_b * numpy.sin(frequency_b* i/158.5 + phaseOffset_b)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(

            bodyIndex = robotId,

            jointName = b'Torso_BackLeg',

            controlMode = p.POSITION_CONTROL,

            targetPosition =  numpy.sin(targetAngles_b[i])*numpy.pi/4,

            maxForce = 100)

    pyrosim.Set_Motor_For_Joint(

            bodyIndex = robotId,

            jointName = b'Torso_FrontLeg',

            controlMode = p.POSITION_CONTROL,

            targetPosition =  numpy.sin(targetAngles_f[i])*numpy.pi/4,

            maxForce = 100)
    time.sleep(1./60.)
    print(backLegSensorValues[i])

    # print(i)
numpy.save("data/backLegSensorValues.txt", backLegSensorValues)
numpy.save("data/frontLegSensorValues.txt", frontLegSensorValues)
numpy.save("data/targetAngles_f.txt", targetAngles_f)
numpy.save("data/targetAngles_b.txt", targetAngles_b)


p.disconnect()