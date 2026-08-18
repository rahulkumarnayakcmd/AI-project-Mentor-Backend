import pyodbc

server = r"ByteLancerLAP\SQLEXPRESS"          # e.g. localhost\SQLEXPRESS
database = "AIProjectMentor"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    connection = pyodbc.connect(connection_string)

    print("SQL Server connection successful!")

    cursor = connection.cursor()
    cursor.execute("SELECT @@VERSION")

    row = cursor.fetchone()
    print(row[0])

    connection.close()

except Exception as e:
    print("Connection failed!")
    print("Error:", e)