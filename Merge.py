import pandas as pd

# Read the race and horse data
race_df = pd.read_csv('Race_info_5-27-2016.csv')
horse_df = pd.read_csv('Horse_info_5-27-2016.csv')

# Merge the dataframes on 'race_id'
merged_df = pd.merge(horse_df, race_df, on='race_id', how='left')

# Write the merged data to a new CSV file
merged_df.to_csv('Merged_info_5-27-2016.csv', index=False)
