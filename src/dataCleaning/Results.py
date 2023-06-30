import csv

# list of column indices you're interested in
column_indices = [2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 38, 519, 520, 521]
column_indices = [i-1 for i in column_indices]
# assuming headers
headers = ['race_id', 'Name', 'Odds', 'FinishPosition', '$2WinPay', '$2PlacePay', '$2ShowPay', 'ExactaPay', 'QuinellaPay',
           'FieldSize', 'track', 'RaceNum', 'Date', 'DistYrds', 'surface', 'TrackCondition', 'ClassDescriptor',
           'Purse', 'Weight', 'PP', 'BettersToteProb', 'BettersToteProbRk', 'BettersToteProbDiff']

race_id = 642
previous_race_number = None
data = []

with open('../../res/memorialDayWeekend2016TestData/results/530res.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        current_race_number = row[13]  # Assuming race number is the 13th field in the row
        if current_race_number != previous_race_number:
            race_id += 1
            previous_race_number = current_race_number
        selected_data = [race_id] + [row[i] for i in column_indices if i < len(row)]  # add race_id to selected data
        data.append(selected_data)

# write selected data to a new file
with open('../../res/memorialDayWeekend2016TestData/results/FormattedResults_5-30-2016.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)  # write your manually defined headers
    writer.writerows(data)  # write the filtered data