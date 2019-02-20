from random import randint
# the amount of bikes at each station, between 0 to 10
Station_A=randint(0,10)
Station_B=15-Station_A
# the amount of bikes on loan
Taken=0
# the number of people attempting to loan at each station per hour
Take_A=3
Take_B=4
# the maximum potential number of returns per hour
Max_Return=7

# for a loop of 24 hours
for n in range(24):
  # attempts to take bikes, possible if station is not empty
  for j in range(Take_A):
    if Station_A>0:
      Station_A-=1
      Taken+=1
  for i in range(Take_B):
    if Station_B>0:
      Station_B-=1
      Taken+=1
  # returning all loaned bikes, up to the value of maximum returns
  if Taken>Max_Return:
    Return=Max_Return
  else:
    Return=Taken
  Taken-=Return
  # half of all returning bikes go to each station
  Return_A=randint(0,Return)
  Return_B=Return-Return_A
  if Return_A+Station_A<=10:
    Station_A+=Return_A
  else:
    Taken+=(Return_A+Station_A)-10
    Station_A=10
  if Return_B+Station_B<=10:
    Station_B+=Return_B
  else:
    Taken+=(Return_B+Station_B)-10
    Station_B=10
  print("StA:",Station_A,"StB:",Station_B, "Taken:", Taken, "Total:",Station_A+Station_B+Taken)