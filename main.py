from flask import Flask, render_template


app = Flask(__name__)


def saveCustomer():
    return "ok"

def removeCustomer():
    return "ok"

def getCustomer():
    return "ok"

def getAllCustomer():
    return "ok"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(None, 3000, True)


