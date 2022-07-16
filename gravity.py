from numpy import float64
import pandas as pd
import csv
import numpy as np
rows = []
with open("final.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)
headers = rows[0]
star_data = rows[1:]
for row in star_data:
    row[2]= float(row[2])*1.989e+30
    row[3] = float(row[3])*6.957e+8    
print(star_data[:10])
star_masses = []
star_radiuses = []
star_name= []
star_distance= []
for row in star_data:
    star_masses.append(row[2])
    star_radiuses.append(row[3])
    star_distance.append(row[1])
    star_name.append(row[0])
star_gravity = []
for index , name in enumerate(star_name):
    gravity = (float(star_masses[index])/( float(star_radiuses[index]) * float(star_radiuses[index])  )) * 6.674e-11
    star_gravity.append(gravity)
print(star_gravity[:10])
data = list(zip(star_name , star_distance , star_masses , star_radiuses , star_gravity))
df = pd.DataFrame(data, columns=["Star_Name" , "Star_Distance" ,"Star_Mass" , "Star_Radiuses" , "Star_Gravity"])
print(df.head())
#################Project 132 ####################################################
