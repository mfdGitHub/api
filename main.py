from flask import Flask, render_template


app = Flask(__name__)

@app.route('/customers/<int:id>') # GET
def getCustomer(id):
    return "ok"
@app.route('/customers') # GET
def getAllCustomers():
    return "ok"

@app.route('/customers', methods=['POST']) # POST
def saveCustomer():
    return "ok"
@app.route('/customers', methods=['DELETE'])
def removeCustomer():
    return "ok"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(None, 3000, True)


