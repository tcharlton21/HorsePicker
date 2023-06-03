from google.cloud import bigquery
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Initialize a BigQuery client
client = bigquery.Client(project = 'horsepicker')

# Query the data from BigQuery
query = """
SELECT _2WinPay, wFig, B, Trainer, Form, Prime
FROM `horsepicker.HorseData.ComprehensiveTable527`
"""
df = client.query(query).to_dataframe()

# Make sure to handle non-numeric data and missing values properly
# Here we fill missing values with 0 and transform categorical variables into integers
df.fillna(0, inplace=True)
le = LabelEncoder()
df[['Trainer']] = df[['Trainer']].apply(lambda col: le.fit_transform(col))

# Split the dataset into features (X) and target (y)
X = df[['Form', 'Prime']]
y = df['_2WinPay']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Print the R-squared on the test data
print("Model R-squared: ", model.score(X_test, y_test))
