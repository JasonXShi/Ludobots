import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

length = 1.0
width = 2.0
height = 3.0

x = 0.0
y = 0.0
z = 1.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[0,1,1.5] , size=[length,width,height])

# for j in range(5):
#     for k in range(5):
#         for i in range(10):
#             pyrosim.Send_Cube(name=str(i), pos=[j,k,0.5+i] , size=[0.9**i*length,0.9**i*width,0.9**i*height])

pyrosim.End()

