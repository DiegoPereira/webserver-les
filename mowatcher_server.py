import json

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/example')
def host_data():

    return 'funfa'

if __name__ == '__main__':
    app.debug = True    
    app.run(host='0.0.0.0', port=9090)
