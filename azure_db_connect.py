
import pyodbc
import csv

connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=redditdataserver.database.windows.net,1433;Database=redditdatadb;Uid=nettles@redditdataserver;Pwd=REDACTED'

# Use .connect (DB API 2.0) to get a Connection Object
conn = pyodbc.connect(connection_string, autocommit=True) # autocommit = True, since it is the SQL Server way

# Create the cursor object
curs = conn.cursor()


# Use the execute method to execute SQL Statements
# Create the table (CPI For All Urban Consumers) / Note the SQL Server specific syntax
curs.execute('''
create table redditdata(
ID int primary key clustered identity(1,1)
,CPIAUCSL varchar(255)
)''')


# Insert some cpi data (R.B.A.R) !
# We are using the .executemany DB API V2.0 Method

insert_query = 'insert into redditdata(CPIAUCSL) values (?)'
with open(r'redditflairdata.csv', 'r', encoding='utf8') as cpi_file:
    cpi = csv.reader(cpi_file)
reddit_data = [row for row in cpi]

curs.executemany(insert_query, reddit_data)


# Commit and close the connection
conn.commit()
conn.close()