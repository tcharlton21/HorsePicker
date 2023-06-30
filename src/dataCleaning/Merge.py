import pandas as pd
import numpy as np

# Read the race and horse data
race_df = pd.read_csv('../../res/memorialDayWeekend2016TestData/horseAndRaceInfo/Race_info_5-30-2016.csv')
horse_df = pd.read_csv('../../res/memorialDayWeekend2016TestData/horseAndRaceInfo/Horse_info_5-30-2016.csv')
results_df = pd.read_csv('../../res/memorialDayWeekend2016TestData/results/FormattedResults_5-30-2016.csv')

# Merge the dataframes on 'race_id'
merged_df = pd.merge(horse_df, race_df, on='race_id', how='left')

# # Merge on both 'race_id'
merged_df = pd.merge(merged_df, results_df, on=['Name'], how='left')
#
#
# # Drop rows with missing data in the results-related columns
# # Change 'result_columns' to the list of your result columns
result_columns = ['FinishPosition']
merged_df = merged_df.dropna(subset=result_columns, how='any')
#
# # Write the merged data to a new CSV file
merged_df.to_csv('Merged_info_5-30-2016.csv', index=False)
