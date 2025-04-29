# Connection details
server = 'dmc2025.database.windows.net'
database = 'Leads'
username = 'atefgh'
password = 'Waxxaw123'
driver = '{ODBC Driver 17 for SQL Server}'

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

# Connect
conn = pyodbc.connect(conn_str)

# Run query
query = "SELECT * FROM your_existing_table"
df = pd.read_sql(query, conn)

# Do your transformation
df=df[["Email Address","Address Line1","City","State","Zip"]]

# Write to new table
df.to_sql('Silver', con=conn, if_exists='replace', index=False, method='multi')  
# OR use cursor.execute() for manual INSERTS if needed



