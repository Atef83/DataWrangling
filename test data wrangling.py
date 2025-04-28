# Connection details
server = 'your-server.database.windows.net'
database = 'your-database'
username = 'your-username'
password = 'your-password'
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
df['new_col'] = df['existing_col'] * 2  # Example transformation

# Write to new table
df.to_sql('your_new_table', con=conn, if_exists='replace', index=False, method='multi')  
# OR use cursor.execute() for manual INSERTS if needed

df=pd.read_excel(r"C:\Users\atefg\Downloads\SegmentDataPreview.xlsx")
silver=df[["Email Address","Address Line1","City","State","Zip"]]
silver
