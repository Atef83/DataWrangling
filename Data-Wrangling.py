import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# Connection details
server = 'dmc2025.database.windows.net'
database = 'Leads'
username = 'atefgh'
password = 'Waxxaw123'
driver = '{ODBC Driver 17 for SQL Server}'

# For reading with pyodbc
conn_str = f"""
DRIVER={driver};
SERVER={server};
DATABASE={database};
UID={username};
PWD={password};
Encrypt=yes;
TrustServerCertificate=no;
Connection Timeout=30;
"""

conn = pyodbc.connect(conn_str)

# Query
query = "SELECT * FROM your_existing_table"
df = pd.read_sql(query, conn)

# Transform
df = df[["Email Address", "Address Line1", "City", "State", "Zip"]]

# For writing with SQLAlchemy
connection_url = f"mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_url)

# Write to new table
df.to_sql('Silver', con=engine, if_exists='replace', index=False, method='multi')
