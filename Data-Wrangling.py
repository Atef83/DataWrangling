from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

server = "dmc2025.database.windows.net"
user = "atefgh"
password = "Waxxaw123"
db_name = "dmc"
dsn = "ODBC Driver 18 for SQL Server"

engine = create_engine(f"mssql+pyodbc://{user}:%s@{server}/{db_name}?TrustServerCertificate=yes&driver={dsn}" % quote_plus(password))

#Connect
conn = engine.connect()


# Run query
query = "SELECT * FROM Leads"
df = pd.read_sql(query, conn)

# Do your transformations
df = df[["Email Address", "Address Line1", "City", "State", "Zip"]]

# Write to new table
df.to_sql('Silver', engine, if_exists='replace', index=False)





