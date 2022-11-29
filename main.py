from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = 'Sup3rR00t.'
app.config['MySQL_DB'] = 'system'
mysql = MySQL(app)

@app.route('/customers') # GET
def getAllCustomers():
    return "Devuelve listado de clientes"

@app.route('/customers/<int:id>') # GET
def getCustomer(id):
    return "Devualve un cliente"

@app.route('/customers', methods=['POST']) # POST
def saveCustomer():
    return "Cliente guardado"
@app.route('/customers/<int:id>', methods=['DELETE'])
def removeCustomer(id):
    return "Cliente eliminado"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(None, 3000, True)


