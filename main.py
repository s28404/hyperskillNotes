# import pandas as pd
# import numpy as np
# from tqdm import tqdm

# df = pd.DataFrame({
#    'Name': ['John', 'Jane', 'Bob', 'Mary', 'Ivan'],
#    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Moscow'],
#    'Age': [32, 25, 47, 19, 45],
#    'Income': [55000, 72000, 89000, 41000, 45000]
# })

# def change_row(row):
#     row['Name'] = row['Name'].upper()
#     row['City'] = row['City'].lower()
#     row['Age'] = row['Age'] + 10
#     row['Income'] = row['Income'] * 1.1
#     return row

# df = df.apply(change_row, axis=1)
# print(df)

# def add_tax(row):
#     if row['Income'] > 60000:
#         tax = row['Income'] * 0.1
#     else:
#         tax = row['Income'] * 0.05
#     return tax

# df['Tax'] = df.apply(add_tax, axis=1)
# print(df)

# def add_suffix(col, suffix):
#     return col + suffix

# # Apply the function to a single column
# df['Name'] = df['Name'].apply(add_suffix, suffix='_Smith')
# print(df)

# def add_value(number):
#     return number + 100

# df[['Income', 'Tax']] = df[['Income', 'Tax']].apply(add_value)
# print(df)

# df_nums = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })

# df_nums['MaxValue'] = df_nums.apply(max, axis=1)

# def calculate_new_income(row):
#     return row['Income'] - row['Tax'] - 100

# df['Income_new'] = df.apply(calculate_new_income, axis=1)

# df['Tax_sqrt'] = df['Tax'].apply(np.sqrt, axis=1)
# print(df)

# df['null_tax'] = df['Tax'].apply(pd.isnull)
# print(df)

# def calculate_tax(income, tax):
#     return pd.Series({'Tax rate': (income / tax) * 100, 'Tax rank': 10000 - tax})

# result_tax = df[['Income', 'Tax']].apply(lambda x: calculate_tax(*x),
# axis=1, result_type='expand')
# print(result_tax)

# def sum_row(row):
#     return row['Income'] + row['Tax']

# result_income_sum = df.apply(sum_row, result_type='reduce', axis=1)
# print(result_income_sum)

# def mean_of_column(col):
#     return col.mean()

# result = df[['Income', 'Tax']].apply(mean_of_column, result_type='broadcast')
# print(result)

# print("TQDM:")
# tqdm.pandas()

# result = df[['Income', 'Tax']].progress_apply(mean_of_column, result_type='broadcast')
# print(result)

# import itertools

# students_maths = ['Ann', 'Kate', 'Tom']
# students_english = ['Tim', 'Carl', 'Dean']
# students_history = ['Jane', 'Mike']

# for student in itertools.chain(students_maths, students_english, students_history):
#     print(student)

# first_list = ['Hi', 'Bye', 'How are you']
# second_list = ['Jane', 'Anton']

# for first, second in itertools.product(first_list, second_list):
#     print(first, second)

# # Trying to create a list containing 10^12 elements will result in a memory
# # too_long_list = list(itertools.product(range(1000000), range(1000000)))

# # However, works with iterators:
# my_iterator=  itertools.product(range(1000000), range(1000000))
# for i in range(5):
#     print(next(my_iterator))

# my_iter = itertools.combinations(range(1, 1000000), 3)

# print("------")
# for i in range(5):
#     print(next(my_iter))
# print("------------")
# all_students = ['Ann', 'Kate', 'Tom', 'Jane', 'Mike', 'Ann', 'Carl', 'Mike']

# all_students.sort()

# for key, group in itertools.groupby(all_students):
#     print(key, list(group))

# all_students.sort(key=lambda x: len(x))

# for key, group in itertools.groupby(all_students, key=lambda x: len(x)):
#     print(key, list(group))
"""
This script demonstrates the usage of various features from the astropy library.
"""

import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.cosmology import FlatLambdaCDM

# Unit Conversion
lengths = np.array([49, 58, 947])
lengths = lengths * u.kilometer
print(lengths)

# Time Conversion
time = 14 * u.hour
print(time.to(u.second))

# Constants (Manually defined G and mu0)
G = 6.67430e-11 * u.m**3 / (u.kg * u.s**2)
mu0 = 4 * np.pi * 1e-7 * u.N / u.A**2
print(mu0.value)
print(mu0)

# Gravitational Force
F = G * 488 * u.kg
print(F)

# SkyCoord
polaris = SkyCoord(ra=37.95456067*u.degree, dec=89.26410897*u.degree, frame='icrs')
print(polaris)

# SkyCoord from Name
aldebaran = SkyCoord.from_name('aldebaran')
print(aldebaran)

# Angular Separation
print(polaris.separation(aldebaran))

# Cosmology (Using FlatLambdaCDM)
my_cosmo = FlatLambdaCDM(H0=67.7, Om0=0.272)
print(my_cosmo)
