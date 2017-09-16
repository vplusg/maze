#A basic agent that plays the game and traverses different paths
class Agent:
  loc_x=0
  loc_y=0
  lives=3
  def __init__(self,x,y):
    self.loc_x=x
    self.loc_y=y
    print("Created Agent")

  #For Unit Testing
  def printAgent(self):
    print("Agent Location = [%s,%s], Lives=%s" % (self.loc_x,self.loc_y,self.lives))

  #To traverse the Maze
  def traverseMaze(self,myMaze,x,y,Path):
    myResult=myMaze.traverse(x,y,Path)
    if myResult==True:
      print("Reached End")
    else:
      if myMaze.REACHED_END==False and myMaze.OUT_OF_LIVES==False:
        print("Out of Lives")
