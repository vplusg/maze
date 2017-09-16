from Agent import Agent
from maze import Maze

with open('./new1.txt') as f:
  lines = f.read().splitlines()
f.close()

for line in lines:
  #Creating Maze Object
  myMaze=Maze(line) 
  #Creating Maze Matrices
  myMaze.makeMaze()

  #Unit Test
  #myMaze.printCellMatrix()
  #Unit Test
  myMaze.printStart()
  #Unit Test
  myMaze.printEnd()

  #Creating Agent that plays the game
  myAgent=Agent(myMaze.getStartX(),myMaze.getStartY())
  #Unit Test
  myAgent.printAgent()

  myAgent.traverseMaze(myMaze, myMaze.getStartX(),myMaze.getStartY(),[])

  print()
print("Game Completed for all three mazes. Thank you!")
