import csv
import pandas as pd

df = pd.read_csv("brown_dwarf_stars.csv")

df = df[df["mass"].notna()]
df = df[df["radius"].notna()]

star_data = df.values.tolist()
for data in star_data:
    data.pop(0)

for sd in star_data:
    print(sd[1])
    sd[3] = float(sd[3])*0.102763
    sd[2] = float(sd[2])*0.000954588

df = pd.DataFrame(star_data, columns = ["name", "distance", "mass", "radius"])
df.to_csv("new_brown_dwarf_stars.csv")