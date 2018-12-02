import pyodbc
from flask import Flask, g, render_template, abort, request


# Globals
connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=redditdataserver.database.windows.net,1433;Database=redditdatadb;Uid=nettles@redditdataserver;Pwd=REDACTED


# Setup Flask
app = Flask(__name__)
app.config.from_object(__name__)

# Before / Teardown
@app.before_request
def before_request():
    try:
        g.sql_conn =  pyodbc.connect(CONNECTION_STRING, autocommit=True)
    except Exception:
        abort(500, "No database connection could be established.")

@app.teardown_request
def teardown_request(exception):
    try:
        g.sql_conn.close()
    except AttributeError:
        pass

# GET All CPI
@app.route('/api/v1/cpi', methods=['GET'])
def get_cpi_data():
    curs = g.sql_conn.cursor()
    query = 'select * from redditdb.dbo.test '
    curs.execute(query)

    columns = [column[0] for column in curs.description]
    data = []


# '/' HTML
@app.route('/')
def api_help():
    return render_template('reddit_news_api.html'), 200


# POST API (Add)
@app.route('/api/v1/cpi', methods=['POST'])
def insertnew():
    data = request.get_json()

    curs = g.sql_conn.cursor()

    query = 'insert redditdb.dbo.test (CPIAUCSL,ObservationDate) VALUES (?,?)'

    if isinstance(data, dict):
        curs.execute(query, data["CPIAUCSL"], data["ObservationDate"])
        curs.commit()

    if isinstance(data, list):
        for row in data:
            curs.execute(query,row["CPIAUCSL"],row["ObservationDate"])
            curs.commit()

    return 'success', 200

# DELETE
@app.route("spi/v1/redditanalysis/<string:id>", method=["DELETE"])
def delete test(id):
    try:
        r.table('test').get.(id).delete().run.(g.rdb_conn)
        return 'success', 200
    except Exception as e:
        return abort(500)


if __name__ == '__main__':
    app.run(host="0.0.0.0")