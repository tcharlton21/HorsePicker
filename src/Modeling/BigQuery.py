from google.cloud import bigquery
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Initialize a BigQuery client
client = bigquery.Client(project='horsepicker')

# Query the data from BigQuery
query = """
SELECT race_id_x, _2WinPay, wFig, B, Trainer, Form, Prime, Odds_x
FROM `horsepicker.HorseData.CmpData`
"""
df = client.query(query).to_dataframe()

# Make sure to handle non-numeric data and missing values properly
# Here we fill missing values with 0 and transform categorical variables into integers
df.fillna(0, inplace=True)
le = LabelEncoder()
df[['Trainer']] = df[['Trainer']].apply(lambda col: le.fit_transform(col))

# Split the dataset into features (X) and target (y)
X = df[['wFig', 'B', 'Trainer', 'Form', 'Prime']]
y = df['_2WinPay']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Print the coefficients and corresponding feature names
coefficients = model.coef_
feature_names = X.columns

for feature, coef in zip(feature_names, coefficients):
    print(f"{feature}: {coef}")


# Predict the target variable for each horse
predictions = model.predict(X)

# Calculate the discrepancy between Odds and predicted values
df['Discrepancy'] = df['Odds_x'] - predictions

# Group the data by race_id and find the horse with the best discrepancy in each race
best_discrepancy_per_race = df.groupby('race_id_x')['Discrepancy'].idxmax()
selected_horses = df.loc[best_discrepancy_per_race]

# Calculate the profit by placing a $2 bet on the selected horses
total_races = len(selected_horses)
total_bet = total_races * 2
total_winnings = selected_horses['_2WinPay'].sum()
profit = total_winnings - total_bet

# Calculate the percentage gained/lost
percentage_gain_loss = (profit / total_bet) * 100

print("Total Races:", total_races)
print("Total Bet:", total_bet)
print("Total Winnings:", total_winnings)
print("Profit:", profit)
print("Percentage Gain/Loss:", percentage_gain_loss)
