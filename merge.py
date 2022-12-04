import csv
import pandas as pd

dataset_1 = []
dataset_2 = []

with open("brightest_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

with open("new_brown_dwarf_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)
    
header_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

header_2 = dataset_2[0].pop(0)
star_data_2 = dataset_2[1:]

for index, sd in enumerate(star_data_2):
    star_data_2[index].pop(0)

final_star_data = []

for sd in star_data_1:
    final_star_data.append(sd)

for sd in star_data_2:
    final_star_data.append(sd)


df = pd.DataFrame(final_star_data, columns = ["name", "distance", "mass", "radius"])
df.to_csv("final.csv")