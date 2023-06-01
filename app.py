from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

server = ''
database = ''
username = ''
password = ''


def create_connection(server, database, username, password):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    return cnxn


@app.route('/')
def get_test():
    connection = create_connection(server, database, username, password)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ')
    rows = cursor.fetchall()

    data = [dict(zip([column[0] for column in cursor.description], row))
            for row in rows]

    connection.close()
    return jsonify(data)

@app.route('/')
def get_test():
    connection = create_connection(server, database, username, password)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ')
    rows = cursor.fetchall()

    data = [dict(zip([column[0] for column in cursor.description], row))
            for row in rows]

    connection.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run()