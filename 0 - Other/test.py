# Supermarket
import random
import numpy
import matplotlib.pyplot as plt
# parameters (by hour)
cashier_count=6
hours=12
wait_line=0
totalcustomer=0
sum_list=[]
hour_list=[]
time_scan_item=5
time_checkout=20
#time of day
# multipliers that have an average of 1
timeday=(0.6,0.6,0.6,0.7,0.8,0.8,1.2,1.4,1.7,1.4,1.2,1.0)
# customer types: young, adults, middle-age, elderly
# list variables: average item per customer, time to check out multiplier22
Item_Time_From_Type={"Young":[4,0.9], "Working":[6,1.0], "Middle":[10,1.0], "Elderly":[5,1.5]}


def customer_in(wait_line,hour):
  global totalcustomer
  customer_input_per_hour=int(random.randint(240,300)*timeday[hour])
  wait_line+=customer_input_per_hour
  totalcustomer+=customer_input_per_hour
  hour_list.append(customer_input_per_hour)
  return wait_line


for n in range(hours):
  wait_line=customer_in(wait_line,n)
  for n in range(cashier_count):
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
      else:
        break
  sum_list.append(totalcustomer)


graph_steps=[n for n in range(9,21)]
plt.plot(graph_steps,sum_list,label="Total customers")
plt.plot(graph_steps,hour_list,label="Customer entered")
plt.legend(loc='upper right')
plt.xlabel("Time (hour of day)")
plt.ylabel("Customer Count")
plt.show()