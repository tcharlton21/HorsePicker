# import bigquery as bigquery
# from google.cloud import bigquery
# from google.oauth2 import service_account
#
# # Set up credentials and project ID
# credentials = service_account.Credentials.from_service_account_file('path/to/credentials.json')
# project_id = 'your-project-id'
#
# # Initialize BigQuery client
# client = bigquery.Client(credentials=credentials, project=project_id)
#
# # Define the dataset and table names
# dataset_id = 'your-dataset-id'
# race_table_id = 'race_info'
# horse_table_id = 'horse_info'
#
# # Specify the path to your CSV files
# race_csv_path = 'path/to/race_info.csv'
# horse_csv_path = 'path/to/horse_info.csv'
#
# # Define the BigQuery schemas for race and horse tables
# race_schema = [
#     bigquery.SchemaField('race_id', 'INTEGER'),
#     bigquery.SchemaField('track', 'STRING'),
#     bigquery.SchemaField('race_number', 'STRING'),
#     bigquery.SchemaField('distance', 'STRING'),
#     bigquery.SchemaField('surface', 'STRING'),
#     bigquery.SchemaField('date_time', 'STRING'),
#     bigquery.SchemaField('race_description', 'STRING'),
#     bigquery.SchemaField('available_bets', 'STRING'),
# ]
#
# horse_schema = [
#     bigquery.SchemaField('race_id', 'INTEGER'),
#     # Add your horse_info column definitions here based on your headers
#     # Example: bigquery.SchemaField('horse_name', 'STRING'),
#     # ...
#
# # Create the race table if it doesn't exist
# race_table_ref = client.dataset(dataset_id).table(race_table_id)
# race_table = bigquery.Table(race_table_ref, schema=race_schema)
# race_table = client.create_table(race_table)  # Will create only if not already exists
#
# # Load race data from CSV into BigQuery
# job_config = bigquery.LoadJobConfig(
#     source_format=bigquery.SourceFormat.CSV,
#     skip_leading_rows=1,
#     autodetect=True,  # Automatically detect schema
# )
# with open(race_csv_path, 'rb') as source_file:
#     load_job = client.load_table_from_file(source_file, race_table_ref, job_config=job_config)
#
# load_job.result()  # Waits for the job to complete
#
# # Create the horse table if it doesn't exist
# horse_table_ref = client.dataset(dataset_id).table(horse_table_id)
# horse_table = bigquery.Table(horse_table_ref, schema=horse_schema)
# horse_table = client.create_table(horse_table)  # Will create only if not already exists
#
# # Load horse data from CSV into BigQuery
# job_config = bigquery.LoadJobConfig(
#     source_format=bigquery.SourceFormat.CSV,
#     skip_leading_rows=1,
#     autodetect=True,  # Automatically detect schema
# )
# with open(horse_csv_path, 'rb') as source_file:
#     load_job = client.load_table_from_file(source_file, horse_table_ref, job_config=job_config)
#
# load_job.result()  # Waits for the job to complete
