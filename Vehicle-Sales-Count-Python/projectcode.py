import pandas as pd
#import xlrd
import matplotlib.pyplot as plt;
import numpy as np


# read csv
df = pd.read_csv("C:\icup assign\MVA_Vehicle_Sales_Counts_by_Month_for_Calendar_Year_2002_-_2019_up_to_August.csv")
# print average
e = []
for i in range(0, 211):
    k = df.iloc[i][2]
    e.append(k)
sums = 0
for i in e:
    sums = sums + i
print('The total no of vehicles sold throughout is:', sums)
print('The average no of vehicles sold per month is:', int(sums / len(e)))
# quarter sales of cars
n = []
for i in range(0, 211, 4):
    g = (df.iloc[i][5] + df.iloc[i + 1][5] + df.iloc[i + 2][5] + df.iloc[i + 3][5])
    n.append(g)
print('The max no of cars sold in a quarter is:', max(n))
print(n.index(max(n)))
print('The quarter in which the sales is most i.e: ', max(n), ' is: ', df.iloc[n.index(max(n)) * 4][1], ' - ',
      df.iloc[n.index(max(n)) * 4 + 3][1], ' of the year: ', df.iloc[n.index(max(n)) * 4][0])
# plot graph
f = []
for v in range(0, 204, 12):
    x = df.iloc[v][4] + df.iloc[v][5]
    f.append(x)
# print(f)
# importing the required module 


# x axis values 
x = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

# plotting the points  
plt.bar(x, f)

# naming the x axis 
plt.xlabel('Year ')
# naming the y axis 
plt.ylabel('Total sales (old + new)')

# giving a title to my graph 
plt.title('total sales in dollars in respective years')

# function to show the plot 
plt.show()
# graph2
labels = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
labels1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG']

# print(df)
gk = df.groupby('Year ')
b = gk.first()
c = gk.get_group(2019)

c1 = gk.get_group(2018)
# create loops of c


# print(c)
d = c['Used']
h = []
e = c['New']
k = []
p = c['Total Sales Used']
o = []
u = c['Total Sales New']
w = []
t = 0
for i in d:
    i = i
    h.append(i)
for i in e:
    i = i
    k.append(i)
for i in p:
    o.append(i)
for i in u:
    w.append(i)

x = np.arange(len(labels))
x1 = np.arange(len(labels1))
width = 0.35
fig, ax1 = plt.subplots()
rects1 = ax1.bar(x1 - width / 2, h, width, label='New')
rects2 = ax1.bar(x1 + width / 2, k, width, label='Used')
ax1.set_ylabel('New/Used vehicles sold')
ax1.set_title('Sales in 2019')
ax1.set_xticks(x1)
ax1.set_xticklabels(labels1)
ax1.legend()

# print(c)
plt.show()
# print(p)
# print(h, k)
