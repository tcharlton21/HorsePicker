import csv

with open("pL_profile.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    race_id = 0