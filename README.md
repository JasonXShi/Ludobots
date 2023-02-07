My fitness functions (in robot.py) finds the longest contiguous number of timesteps where all 6 legs of my hexapod robot are not in contact with the ground. I do this using the stored values of the touch sensors.

In my PHC, I am selecting for the greatest fitness value, which corresponds to the longest time in the air. I am trying to make my robot jump as high as possible, which you can see is successful in the YouTube video. The first clip shows an unevolved robot, that fails to get off the ground. The second clip shows the evolved robot that leaps into the air (after 10 generations of 20 population size).

Run search.py to see the results. (you may have to change python to python3, depending on your system)