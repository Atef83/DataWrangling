import jaydebeapi
import pandas as pd

server = 'dmc2025.database.windows.net'
database = 'Leads'
username = 'atefgh'
password = 'Waxxaw123'

jdbc_url = f"jdbc:sqlserver://{server}:1433;databaseName={database};encrypt=true;trustServerCertificate=false"
driver_class = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
jar_file = "jdbc_driver/sqljdbc_12.6/enu/mssql-jdbc-12.6.1.jre11.jar"  # Match extracted file

conn = jaydebeapi.connect(
    driver_class,
    jdbc_url,
    [username, password],
    jar_file
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM your_existing_table")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(rows, columns=columns)
