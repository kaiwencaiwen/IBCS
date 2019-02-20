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
item_time_from_type={"Young":[4,0.9], "Working":[6,1.0], "Middle":[10,1.0], "Elderly":[5,1.5]}

# function for introducing customers
def customer_in(wait_line,hour):
 global totalcustomer
# a random value of customers is chosen and scaled depending on the time of day
 customer_input_per_hour=random.randint(240,300)
 customer_input_per_hour=int(customer_input_per_hour*timeday[hour])
 wait_line+=customer_input_per_hour
 totalcustomer+=customer_input_per_hour
 hour_list.append(customer_input_per_hour)
 return wait_line

# one step is complete every hour
for n in range(hours):
# calls the customer_in function that adds an amount of customers to the purchase queue
 wait_line=customer_in(wait_line,n)
# each cashier services a certain amount of customers per hour
 for n in range(cashier_count):
# each cashier has 3600 seconds (1 hour) to service as any customers as possible, each customer takes different amounts of time to checkout
    time_left=3600
    while wait_line>0:
        # the customer is given to be one of 4 age groups
        customer_type=numpy.random.choice(["Young", "Working", "Middle", "Elderly"], p=[0.1,0.3,0.4,0.2])
        items_per_customer, checkout_multiplier=item_time_from_type[customer_type]
        required_time=(items_per_customer+random.randint(-3,3))*time_scan_item+(checkout_multiplier+2*random.random()-1)*time_checkout
        if time_left>required_time:
            time_left-=required_time
            # the queue is decreased by 1
            wait_line-=1
        else:
            break
 sum_list.append(totalcustomer)

# graphing
graph_steps=[n for n in range(9,21)]
plt.plot(graph_steps,sum_list,label="Total customers")
plt.plot(graph_steps,hour_list,label="Customer entered")
plt.legend(loc='upper right')
plt.xlabel("Time (hour of day)")
plt.ylabel("Customer Count")
plt.show()







