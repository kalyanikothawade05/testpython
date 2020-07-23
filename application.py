import pyodbc
from flask import Flask, request,json

app = Flask(__name__)
#app.config.from_object(app_config)
#Session(app)
@app.route("/")
#SQL connection & fetech 
def indexfun():
    server ='tcp:ewmtest.database.windows.net'
    database ='POCDatapoints'
    username ='kunalpoc'
    password ='Akshaypoc123'
    driver='{ODBC Driver 17 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM poctest")
    row = cursor.fetchone()
    prediction_percentage = []
    timestamp = []
    while row:
        print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
        x = str(row[3])
        prediction_percentage.append(x)
        y = str(row[0])
        timestamp.append(y)
        row = cursor.fetchone()
    result_dict = {}
    result_dict['prediction_percentage'] = prediction_percentage
    result_dict['timestamp'] = timestamp
    response = app.response_class(
            response=json.dumps(result_dict),
            status=200,
            mimetype='application/json'
            )
    return response   
#return JSON
  
if __name__ == "__main__":
   app.run()
