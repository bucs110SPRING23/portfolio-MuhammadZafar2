#Part A
weeks = 16
classes = 5
tuition = 6000
classes_per_week= 3
cost_per_week = ((tuition / classes) / weeks)
cost_per_class= cost_per_week/ classes_per_week
print("Cost per week:", cost_per_week)
print("Every time you go to class you give:", cost_per_class)

print(weeks, type(weeks)) 
print(classes, type(classes)) 
print(tuition, type(tuition)) 
print(classes_per_week, type(classes_per_week)) 
print(cost_per_week, type(cost_per_week)) 
print(cost_per_class, type(cost_per_class)) 

#Part B
import random
random.randint(1,10) #non-inclusive?
random_lists= ["hello",
"bye",
5.0,
3,
56
]
randomizing_my_list=random.choice(random_lists)
print(randomizing_my_list)