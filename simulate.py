from simulation import SIMULATION
import sys

simulation = SIMULATION(sys.argv[1], sys.argv[2])

simulation.Run()

simulation.Get_Fitness()

# import pybullet as p
# import pybullet_data
# import time
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import constants as c

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.stepSimulation()

# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)
# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)

# targetAngles_f = numpy.linspace(0, 2*numpy.pi, 1000)
# # targetAngles = numpy.sin(targetAngles)

# for i in range(1000):
#     targetAngles_f[i] = c.amplitude_f * numpy.sin(c.frequency_f* i/158.5 + c.phaseOffset_f)

# targetAngles_b = numpy.linspace(0, 2*numpy.pi, 1000)
# # targetAngles = numpy.sin(targetAngles)

# for i in range(1000):
#     targetAngles_b[i] = c.amplitude_b * numpy.sin(c.frequency_b* i/158.5 + c.phaseOffset_b)

# for i in range(1000):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(

#             bodyIndex = robotId,

#             jointName = b'Torso_BackLeg',

#             controlMode = p.POSITION_CONTROL,

#             targetPosition =  numpy.sin(targetAngles_b[i])*numpy.pi/4,

#             maxForce = 100)

#     pyrosim.Set_Motor_For_Joint(

#             bodyIndex = robotId,

#             jointName = b'Torso_FrontLeg',

#             controlMode = p.POSITION_CONTROL,

#             targetPosition =  numpy.sin(targetAngles_f[i])*numpy.pi/4,

#             maxForce = 100)
#     time.sleep(1./60.)
#     print(backLegSensorValues[i])

#     # print(i)
# numpy.save("data/backLegSensorValues.txt", backLegSensorValues)
# numpy.save("data/frontLegSensorValues.txt", frontLegSensorValues)
# numpy.save("data/targetAngles_f.txt", targetAngles_f)
# numpy.save("data/targetAngles_b.txt", targetAngles_b)


# p.disconnect()