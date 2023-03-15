# Ludobots

Overview:
In this assignment, I evolved 10 seeds with a population size of 10 and 500 generations to move the furthest distance from (0,0). To run the program, run the make_horse.py file. 

2 Minute Summary Video:




10 Second Teaser Gif:

![Untitled video - Made with Clipchamp (3)](https://user-images.githubusercontent.com/12127463/225207722-b9839baf-c104-4f57-9f44-b62a45136089.gif)


Sim Count: 50,000+

I ran 10 simulations with 500 generations and 10 population size. The fitness graphs for these simulations are here: https://docs.google.com/document/d/1Qr4omJ0T2rvjbqmTKlFaEyeMHZjNmgNE3qevkng9Hv0/edit?usp=sharing
Each simulation with 500 generations and 10 population size took me around 20 minutes to complete. 

Laws of Physics Are Obeyed: Body is randomly generated and obeys all the laws of physics. Mutation is also random.

Methods:

Fitness Value Used: Euclidean distance from (0,0)

Explanation of Codebase: I used the parallelHillClimber.py to evolve 10 populations of 500 generations, which generated bodies and brains according to solution.py (diagrams below). 
In order to run 50,000 simulations, I ran my parallelHillClimber.py 10 times in total. Selection is handled by the parallelHillClimber.py, where it replaces the parent of each generation if the parent has any children with better fitness than it. 

Generation and Mutation Diagrams:

![image](https://user-images.githubusercontent.com/12127463/225203595-bafa0faf-9f73-4b76-b325-50c2a5c96d6a.png)

![image](https://user-images.githubusercontent.com/12127463/225203636-14f891df-4200-4871-ac54-9d48e4ed6472.png)

Results: 

 Example fitness graph of 5000 simulations: (500 generations of 10 population size)
 
 ![image](https://user-images.githubusercontent.com/12127463/225204159-010264d9-d468-44e8-962f-2fe0f707816c.png)
 
 As you can see, as the simulations keep running, the number of beneficial mutations decreases. I hypothesize that this is due to my mutations frequently not being beneficial. My possible mutations were additional cubes, and changing the size of the cubes.
 Even though my mutate function worked properly for changing the size and quantity of cubes, as you can see in my video, it doesn't drastically increase the movement in my robot. 
 In the end, too many cubes would also work against smooth movement, although there are more motors, there is also higher chance of being stuck.

From this graph, you can see that in the beginning there are more robots that have a lower amount of movement, but towards the end of the 5,000 simulations, there are less robots that can move, but the ones that can move, usually move more than the robots in the beginning.
 
 All 10 Fitness Graphs: https://docs.google.com/document/d/1Qr4omJ0T2rvjbqmTKlFaEyeMHZjNmgNE3qevkng9Hv0/edit?usp=sharing
 
 
 Citations:
 
 Coding tutorials by reddit.com/r/ludobots
 
 Pyrosim by https://github.com/jbongard/pyrosim
