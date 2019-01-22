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

# customer input by time of day: multipliers that have an average of 1
timeday=(0.6,0.6,0.6,0.7,0.8,0.8,1.2,1.4,1.7,1.4,1.2,1.0)
# customer types: young, adults, middle-age, elderly
# variables: average item per customer, time to check out multiplier
Item_Time_From_Type={"Young":[4,0.9], "Working":[6,1.0], "Middle":[10,1.0], "Elderly":[5,1.5]}

# function for introducing new customers at the start of each hour
def customer_in(wait_line,hour):
  global start_time
  ###global totalcustomer
  customer_input_per_hour=int(random.randint(240,300)*timeday[hour])
  start_time+=[hour+1]*customer_input_per_hour
  ###print(customer_input_per_hour,"customers introduced")
  wait_line+=customer_input_per_hour
  return wait_line

# the code is ran to graph 1 to 10 cashiers
for cashier_count in range(1,max_cashier+1):
  start_time=[]
  end_time=[]
  wait_line=0
  full_time_list=[]
  for n in range(hours):
    ###print("at hour",n+1,":")
    wait_line=customer_in(wait_line,n)
    for i in range(cashier_count):
      time_left=3600
      while wait_line>0:
        # customer=random.randint(0,100)
        # if customer<=100:
        customer_type=numpy.random.choice(["Young", "Working", "Middle", "Elderly"], p=[0.1,0.3,0.4,0.2])
        items_per_customer,checkout_multiplier=Item_Time_From_Type[customer_type]
        #print(items_per_customer,Time_Multiplier)
        required_time=(items_per_customer+random.randint(-3,3))*time_scan_item+(checkout_multiplier+2*random.random()-1)*time_checkout
        if time_left>required_time:
          time_left-=required_time
          wait_line-=1
          end_time.append(n+1)
        else:
          break
    full_time_list.append(wait_line)
  graph_queue_size.append(full_time_list)

print(graph_queue_size)
print(start_time)
print(end_time)
###print(totalcustomer)

graph_steps=[n for n in range(1,13)]
for n in range(max_cashier):
  cashier_label="Cashiers:"+str(n+1)
  plt.plot(graph_steps,graph_queue_size[n],label=cashier_label)
plt.legend(loc='upper right')
plt.xlabel("Time (hour of day)")
plt.ylabel("Queue Size")
plt.show()