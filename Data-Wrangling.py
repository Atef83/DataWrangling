import jaydebeapi
import pandas as pd

# Connection string details
server = 'dmc2025.database.windows.net'
database = 'Leads'
username = 'atefgh'
password = 'Waxxaw123'

jdbc_url = f"jdbc:sqlserver://{server}:1433;databaseName={database};encrypt=true;trustServerCertificate=false"
driver_class = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
jar_file = "sqljdbc.jar"

# Connect using JDBC
conn = jaydebeapi.connect(
    driver_class,
    jdbc_url,
    [username, password],
    jar_file
)

# Example: fetch data
cursor = conn.cursor()
cursor.execute("SELECT * FROM your_existing_table")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(rows, columns=columns)

# Transform + Write (manual insert or via sqlalchemy alt)
df = df[["Email Address", "Address Line1", "City", "State", "Zip"]]
