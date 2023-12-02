# import matplotlib.pyplot as plt

# from sklearn import datasets
# from sklearn import svm

# digit = datasets.load_digits()

# print(digit.data)

import numpy as np 
import matplotlib.pyplot as plt 

years = ["2016", "2017", "2018", "2019"]
cats = np.array([50, 45, 37, 30])
dogs = np.array([40, 39, 50, 55])
hamsters = np.array([10, 16, 13, 15])
  
# create x-axis values depending on the number of years
x_axis = np.arange(len(years))

# increase the figure size 
plt.figure(figsize=(12, 8))

# plt.bar(x_axis-0.2, cats, width=0.4, label='Cats')
# plt.bar(x_axis+0.2, dogs, width=0.4, label='Dogs')
  
films = ['Wonder Woman', 'Sonic', '1917', 'Star Wars', 'Onward']
box_office = [16.7, 26.1, 37.0, 34.5, 10.6]

# plotting the chart horizontally
plt.barh(films, box_office)
  
# plt.bar(years, cats, label='Cats')
# plt.bar(years, dogs, bottom=cats, label='Dogs')
# plt.bar(years, hamsters, bottom=cats+dogs, label='Hamsters')

# set tick labels and their location
plt.xticks(x_axis, years)

plt.xlabel('Years', fontsize=14)
plt.ylabel('Preference (%)', fontsize=14)
plt.title('The results of cat/dog survey', fontsize=20)

# add legend 
plt.legend()

plt.show()