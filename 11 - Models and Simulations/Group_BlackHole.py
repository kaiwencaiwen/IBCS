from random import randint
import random
# the costs and reward parameters of the game
stepmoney=1
endmoney=25
paymoney=10
# initialized values for repeated trials, positions
trials=10000
xpos=-1
ypos=-1
# function that creates a grid (2D array) of 3 black holes, 1 start and 1 goal
def grid_init():
  global xpos,ypos
  grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  start=False
  while not start:
    xcoord=randint(0,3)
    ycoord=randint(0,3)
    if grid[xcoord][ycoord]==0:
      grid[xcoord][ycoord]=1
      xpos=xcoord
      ypos=ycoord
      start=True
  goal=False
  while not goal:
    xcoord=randint(0,3)
    ycoord=randint(0,3)
    if grid[xcoord][ycoord]==0:
      grid[xcoord][ycoord]=2
      goal=True
  blackholes=0
  while blackholes<3:
    xcoord=randint(0,3)
    ycoord=randint(0,3)
    if grid[xcoord][ycoord]==0:
      grid[xcoord][ycoord]=3
      blackholes+=1
  return grid
# for every step, a random move is chosen from possible moves from that position (bounded by the grid)
def stepping(xpos,ypos):
    possible_moves = []
    if xpos != 3:
        possible_moves.append(0)
    if xpos != 0:
        possible_moves.append(1)
    if ypos != 3:
        possible_moves.append(2)
    if ypos != 0:
        possible_moves.append(3)
    move_choice = random.choice(possible_moves)
    if move_choice == 0:
        xpos += 1
    elif move_choice == 1:
        xpos -= 1
    elif move_choice == 2:
        ypos += 1
    else:
        ypos -= 1
    return xpos,ypos
# a full run shows the monetary return of 1 game
def fullrun():
  global xpos,ypos
  grid=grid_init()
  #for row in grid:
    #print(row)
  money=0
  dead=False
  while not dead:
    xpos,ypos=stepping(xpos,ypos)
    onblock=grid[xpos][ypos]
    # move 1 step, until a black hole is touched
    if onblock==3:
      break
    # every safe step, money is raised by one
    elif onblock==0:
      money+=stepmoney
    # if the goal is touched, the game ends and the money is raised by 25
    elif onblock==2:
      money+=stepmoney+endmoney
      break
  return money

# find the average return over a large number of trials
totalmoney=0
for n in range(trials):
  totalmoney+=fullrun()
print("Average earned: $",totalmoney/trials)

print("Estimated profit per game: $",(totalmoney/trials)-paymoney)