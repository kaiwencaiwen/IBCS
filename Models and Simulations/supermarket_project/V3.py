# Supermarket
import random
import numpy
import matplotlib.pyplot as plt
# Parameters
max_cashier=10
hours=12
wait_line=0
time_scan_item=5
time_checkout=20
graph_queue_size=[]
# to calculate the time that each customer waits, 3 lists are employed
# graph_start records the hour at which each customer enters the supermarket, for different amounts of cashiers
graph_start=[]
# graph_start records the hour at which each customer completes the purchase, for different amounts of cashiers
graph_end=[]
# graph_wait calculates the difference
graph_wait=[]
timeday=(0.6,0.6,0.6,0.7,0.8,0.8,1.2,1.4,1.7,1.4,1.2,1.0)
Item_Time_From_Type={"Young":[4,0.9], "Working":[6,1.0], "Middle":[10,1.0], "Elderly":[5,1.5]}

def customer_in(wait_line,hour):
 global start_time
 customer_input_per_hour=int(random.randint(240,300)*timeday[hour])
# x customers are introduced at hour n, the graph_start appends x values of n+1 (since n starts 0)
 start_time+=[hour+1]*customer_input_per_hour
 wait_line+=customer_input_per_hour
 return wait_line

# the code is ran to graph 1 to 10 cashiers
for cashier_count in range(1,max_cashier+1):
 # start_time records the hour at which each customer enters the supermarket
 start_time=[]
 # end_time records the hour at which each customer completes the purchase
 end_time=[]
 wait_line=0
 full_time_list=[]
 for n in range(hours):
   wait_line=customer_in(wait_line,n)
   for i in range(cashier_count):
     time_left=3600
     while wait_line>0:
       customer_type=numpy.random.choice(["Young", "Working", "Middle", "Elderly"], p=[0.1,0.3,0.4,0.2])
       items_per_customer,checkout_multiplier=Item_Time_From_Type[customer_type]
       required_time=(items_per_customer+random.randint(-3,3))*time_scan_item+(checkout_multiplier+2*random.random()-1)*time_checkout
       if time_left>required_time:
         time_left-=required_time
         wait_line-=1
# each time a purchase is completed, end_time is appended by 1 value of the n+1th hour (since n starts 0)
         end_time.append(n+1)
       else:
         break
   full_time_list.append(wait_line)
 graph_queue_size.append(full_time_list)
# for each amount of cashier, the list of start and end times are appended to the 2D array
 graph_start.append(start_time)
 graph_end.append(end_time)

# the difference in start and end times are calculated to calculate the time each customer has to wait for
for n in range(max_cashier):
 wait_time_list=[]
 for k in range(len(graph_start[n])):
   try:
       wait_time=graph_end[n][k]-graph_start[n][k]
   except:
       wait_time=12-graph_start[n][k]
   wait_time_list.append(wait_time)
 graph_wait.append(wait_time_list)

# a dictionary is constructed for different amounts of cashiers, to calculate the frequencies of different wait times
dict_wait=[]
for n in range(max_cashier):
   dictoftime={}
   for k in(graph_wait[n]):
       try:
           dictoftime[k]+=1
       except:
           dictoftime[k]=1
   print(n+1," cashiers ",end="")
   print(dictoftime)
   dict_wait.append(dictoftime)

# output in a format that can be transferred to spreasheet
for n in range(9):
    for wdict in dict_wait:
        try:
            print(wdict[n],end=" ")
        except:
            print(0,end=" ")
    print()

