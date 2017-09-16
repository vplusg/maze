from Agent import Agent

class Maze:
  UP = 1
  RIGHT = 2
  DOWN = 4
  LEFT = 8
  START = 16
  END = 32
  MINE = 64
  endX=0
  endY=0
  startX=0
  startY=0
  lives=3
  size_list=[0,0]
  REACHED_END=False
  OUT_OF_LIVES=False
  Maze_Matrix = [[0 for x in range(size_list[0])] for y in range(size_list[1])]  
  Cell_Matrix = [[cell_dict for x in range(size_list[0])] for y in range(size_list[1])]  
  Was_Here = [[False for x in range(size_list[0])] for y in range(size_list[1])]
  Path=[]
  line=""

  def __init__(self,line):
    self.line=line
    print("Creating Maze")

  def printLocalCellMatrix(self,Cell_Matrix):
    print(Cell_Matrix)

  def makeMaze(self):
    cell_dict={"up":False,"right":False,"down":False,"left":False,"start":False,"end":False,"mine":False}

    #Unit Test: Read in the file
    #with open('./new1.txt') as f:
    #  lines = f.read().splitlines()

    print(self.line)
    size,maze=self.line.split('-')
    #print("size = %s, maze = %s" % (size,maze))

    #Extracting size information
    for char in size:
      if char in "()":
          size=size.replace(char,'')
    #print("size",size)
    size_list=size.split(",")
    for i in range(len(size_list)):
      size_list[i]=int(size_list[i])
    self.size_list=list(size_list)

    #Extracting structure information
    for char in maze:
      if char in "[]":
        maze=maze.replace(char,'')
    maze_list=maze.split(",")
    for i in range(len(maze_list)):
      maze_list[i]=int(maze_list[i])

    #print("size_list = %s, maze_list = %s" % (size_list,maze_list))

    Maze_Matrix = [[0 for x in range(size_list[0])] for y in range(size_list[1])]  
    self.Maze_Matrix=list(Maze_Matrix)

    #Matrix for holding meaningfull information after bitwise and operations
    Cell_Matrix = [[cell_dict for x in range(size_list[0])] for y in range(size_list[1])]  
    self.Cell_Matrix=list(Cell_Matrix)

    #Matrix to keep a track of the path followed to prevent overlap
    Was_Here = [[False for x in range(size_list[0])] for y in range(size_list[1])]
    self.Was_Here=list(Was_Here)
    #Unit Test
    #self.printWas_Here()

    #Populating the maze per the instructions in the pdf file
    k=0
    for y in range(size_list[1]):
      for x in range(size_list[0]):
        Maze_Matrix[y][x]=maze_list[k]
        k+=1

    # Doing bit wise operation and creating a more meaningful matrix for the maze
    for y in range(size_list[1]):
      for x in range(size_list[0]):
        cell_dict={"up":False,"right":False,"down":False,"left":False,"start":False,"end":False,"mine":False}
        if self.UP&Maze_Matrix[y][x]==self.UP:
          cell_dict["up"]=True
        if self.RIGHT&Maze_Matrix[y][x]==self.RIGHT:
          cell_dict["right"]=True
        if self.DOWN&Maze_Matrix[y][x]==self.DOWN:
          cell_dict["down"]=True
        if self.LEFT&Maze_Matrix[y][x]==self.LEFT:
          cell_dict["left"]=True
        if self.START&Maze_Matrix[y][x]==self.START:
          cell_dict["start"]=True
          self.setStart(x,y)
        if self.END&Maze_Matrix[y][x]==self.END:
          cell_dict["end"]=True
          self.setEnd(x,y)
        if self.MINE&Maze_Matrix[y][x]==self.MINE:
          cell_dict["mine"]=True
        Cell_Matrix[y][x]=cell_dict
    #Unit Test
    #self.printLocalCellMatrix(Cell_Matrix)
    self.Cell_Matrix = list(Cell_Matrix)
    print("Maze Created")

  def setStart(self,x,y):
    self.startX=x
    self.startY=y
  
  def getStartX(self):
    return self.startX
  def getStartY(self):
    return self.startY

  def setEnd(self,x,y):
    self.endX=x
    self.endY=y
  def getEndX(self):
    return self.endX
  def getEndY(self):
    return self.endY


#Unit Test
  def printEnd(self):
    print("End location = [%s,%s]" % (self.endX,self.endY))

#Unit Test
  def printStart(self):
    print("Start location = [%s,%s]" % (self.startX,self.startY))
    
#Unit Test
  def printCellMatrix(self):
    print(self.Cell_Matrix)

#Unit Test
  def printWas_Here(self):
    print("x=%s,y=%s" % (self.size_list[0],self.size_list[1]))
    for y in range(self.size_list[1]):
      for x in range(self.size_list[0]):
        print(x,y,self.Was_Here[y][x])

  # I am using the recursive maze solution algorithm 
  # But I have not copied from internet
  # I have written this from scratch during my assignment work today
  # I am not including randomness in which path to pick if there are more 
  # than one path in a cell so that I can troubleshoot and determine if
  # the algorithm is working fine. Hence its possible that results maybe
  # same for multiple runs. I am also making the assumption that whichever
  # result occurs first - "Reaching the end" or "Running out of lives"
  # I will publish that and once a run reaches end of lives I wont attempt to 
  # run another path to find the end. 

  def traverse(self,x,y,Path):
    #Unit Test
    #print("In Traverse",x,y)
    if x==self.getEndX() and y==self.getEndY():
      print("Reached End. Path = %s" % (Path))
      self.REACHED_END=True 
      return True
    
    if self.Was_Here[y][x]==False:
      self.Was_Here[y][x]=True
      #print(self.lives,x,y,self.Cell_Matrix[y][x])
      try:
        if self.lives>0:
          if self.Cell_Matrix[y][x]["left"]==True:
            if x>0:
              Path.append("left")
              self.traverse(x-1,y,Path)
          if self.Cell_Matrix[y][x]["right"]==True:
            if x< self.size_list[0]:
              Path.append("right")
              self.traverse(x+1,y,Path)
          if self.Cell_Matrix[y][x]["up"]==True:
            if y>0:
              Path.append("up")
              self.traverse(x,y-1,Path)
          if self.Cell_Matrix[y][x]["down"]==True:
            if y<int(self.size_list[1]):
              Path.append("down")
              self.traverse(x,y+1,Path)
          if self.Cell_Matrix[y][x]["mine"]==True:
            self.lives-=1
          return False
        else:
          #This will print only if it reached the end of all lives
          if self.REACHED_END==False:
            if self.OUT_OF_LIVES==False:
              print("Out of lives. Path = %s" % (Path))
            self.OUT_OF_LIVES=True
            return False
      except RecursionError:
        print("Too many recursions")
        exit(0)
    else:
      return False      
      
   
