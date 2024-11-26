# Python Homework 2
# Matthew Acs
# COP 4020

import numpy as np
import pandas as pd

# (1)  Move the show_results.txt file from Canvas into your project 
# directory. 

print("------------------------------------- 1")
# (2)  Create 3 lists, one for states, one for shows, and one for viewers. 
states = []
shows = []
viewers = []

print("------------------------------------- 2")
# (3)  Injest data from text file and put it into a NumPy array 
# (show_results.txt) 
# Itll look like a nested list.   
# [ [‘Oregon’, ‘Once Upon a Time’, ‘4075’] [...] ...] 
data = np.genfromtxt('show_results.txt', dtype='str', delimiter=',')

print("------------------------------------- 3")
# (4)  Print the raw data 
print(data)

print("------------------------------------- 4")
# (5)  Take the data from the NumPy array and sort it by state, show and 
# viewers, putting each into the appropriate lists you defined earlier.  
# (so now you have 3 lists, one with states, one with shows and one 
# with viewer counts.)  No duplicates in the states and shows.  
# Duplicates can and should exist in the viewers.  So the states list will 
# look like this: ['Washington', 'Nevada', 'Idaho', 
# 'California', 'Oregon'] 
for x in data:
    if x[0] not in states:
        states.append(x[0])
    if x[1] not in shows:
        shows.append(x[1])
    viewers.append(x[2])

print("------------------------------------- 5")    
# (6)  Print these unsorted lists 
print(states)
print("")
print(shows)
print("")
print(viewers)

print("------------------------------------- 6")
# (7)  Convert all 3 lists into NumPy arrays 
states = np.asarray(states)
shows = np.asarray(shows)
viewers = np.asarray(viewers)

print("------------------------------------- 7")
# (8)  print new NumPy Arrays 
print(states)
print("")
print(shows)
print("")
print(viewers)

print("------------------------------------- 8")
# (9)  Sort the States and Shows arrays 
#  Now your States array will look like: 
#  ['California', 'Idaho', 'Nevada', 'Oregon', 
# 'Washington'] 
states = np.sort(states) 
shows = np.sort(shows)
## states = np.unique(data[:, 0]) - Easy way to remove duplicates and sort array at the same time

print("------------------------------------- 9")
# (10)  Convert the Viewers array from STRINGS into INTS 
viewers = viewers.astype(int)

print("------------------------------------- 10")
# (11)  Sum up viewers list into one variable (you can do this in one 
# line) 
viewers_sum = np.sum(viewers)

print("------------------------------------- 11")
# (12)  Print: Sorted arrays (states and shows), viewers list (as ints), 
# and the variable that is the sum of the viewers list. 
print(states)
print("")
print(shows)
print("")
print(viewers)
print("")
print(viewers_sum)

print("------------------------------------- 12")
# (13)  Create 2 DataFrames: 
# (a) show_raw_stats: index = numpy sorted array of SHOWS; 
# columns = numpy sorted array of STATES 
# (b) show_agg_stats: index = same as above; columns= a list with 
# the words Max, Min, Totals and Percent in it (like this... 
# [‘Max’,’Min’,’Totals’, ‘Percent’]
show_raw_stats = pd.DataFrame(0, index=shows, columns=states)
show_agg_stats = pd.DataFrame(0, index=shows, columns=['Max','Min','Totals','Percent'])

print("------------------------------------- 13")
# (14)  Populate show_raw_stats with data from the Original Array 
# injested from show_results.txt. 
# (a) HINT:  You will need to create a loop here that basically goes 
# the length of the original array, and on each iteration, it grabs 
# the STATE, SHOW, and VIEWERS number (itll be a string so 
# youll have to convert it...).  The final step of each iteration will 
# be placing it in the dataframe in the correct spot as an 
# accumulation. +=      (Otherwise you just writing over the value 
# there)   (Remember the lecture where we used df.ix...) 
for x in data:
    show_raw_stats.loc[x[1]][x[0]] += int(x[2])

print("------------------------------------- 14")
# (15)  Populate the Max, Min, Totals, and Percent in show_agg_stats 
# using the DataFrame native functionality (see lecture)     
show_agg_stats['Max'] = show_raw_stats.max(axis = 1)
show_agg_stats['Min'] = show_raw_stats.min(axis = 1)
show_agg_stats['Totals'] = show_raw_stats.sum(axis = 1)
show_agg_stats['Percent'] = (show_raw_stats.sum(axis = 1).divide(viewers_sum)) * 100

print("------------------------------------- 15")
# (16)  Print both dataframe 
print(show_raw_stats)
print(show_agg_stats)

print("------------------------------------- 16")
# (17)  Print the answer to these questions: 
# (a) Which Show has the highest percentage? 
# (b) Which Show has the lowest percentage? 
# (c) Which show is your favorite?
max_percentage = show_agg_stats['Percent'].max()
min_percentage = show_agg_stats['Percent'].min()
for x in range(10):
    if show_agg_stats['Percent'][x] == max_percentage:
        max_show = show_agg_stats.index[x]
    if show_agg_stats['Percent'][x] == min_percentage:
        min_show = show_agg_stats.index[x]

print(max_show + " has the highest percentage.")
print("")
print(min_show + " has the lowest percentage.")
print("")
print("The Flash is my favorite show.")

print("------------------------------------- 17")
