import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.txt.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.txt.npy")
targetAngles_f = numpy.load("data/targetAngles_f.txt.npy")
targetAngles_b = numpy.load("data/targetAngles_b.txt.npy")


# matplotlib.pyplot.plot( backLegSensorValues, label="Back Leg", linewidth=3.0 )
# matplotlib.pyplot.plot( frontLegSensorValues , label="Front Leg" )
matplotlib.pyplot.plot( targetAngles_f, label="targetAngles" )
matplotlib.pyplot.plot( targetAngles_b, label="targetAngles" )


print(backLegSensorValues)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

