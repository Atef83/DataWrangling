import jaydebeapi
import pandas as pd

# Connection details
server = 'dmc2025.database.windows.net'
database = 'Leads'
username = 'atefgh'
password = 'Waxxaw123'
driver = 'com.microsoft.sqlserver.jdbc.SQLServerDriver'
jar_file = 'path_to_mssql_jdbc_auth-8.4.1.x86_64.jar'  # Download the JDBC driver

conn_str = f"jdbc:sqlserver://{server}:1433;databaseName={database};user={username};password={password};encrypt=true;trustServerCertificate=false;"

# Connect
conn = jaydebeapi.connect(
    driver,
    conn_str,
    jars=jar_file
)

# Run query
query = "SELECT * FROM your_existing_table"
df = pd.read_sql(query, conn)

# Do your transformation
df = df[["Email Address", "Address Line1", "City", "State", "Zip"]]

# Write to new table
# Since jaydebeapi doesn't play nicely with pandas to_sql,
# you might need to use a different approach, like executemany or manual INSERTS
cursor = conn.cursor()
# Create table
cursor.execute('''
    IF OBJECT_ID('Silver', 'U') IS NOT NULL 
    DROP TABLE Silver;

    CREATE TABLE Silver (
        "Email Address" VARCHAR(255),
        "Address Line1" VARCHAR(255),
        "City" VARCHAR(255),
        "State" VARCHAR(255),
        "Zip" VARCHAR(255)
    );
''')

# Insert data
insert_query = '''
    INSERT INTO Silver ("Email Address", "Address Line1", "City", "State", "Zip")
    VALUES (?, ?, ?, ?, ?)
'''

# Convert df to list of tuples
data = list(df.itertuples(index=False, name=None))

# Execute many
cursor.executemany(insert_query, data)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()