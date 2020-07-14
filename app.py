# testpython
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello Flask, on Azure App Service for Linux"
 
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 80)


