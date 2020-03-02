from flask import Flask, render_template, session, url_for, redirect, flash, request
from flask_cors import CORS, cross_origin
import simplejson as json

app = Flask(__name__)
cors = CORS(app)

@app.route('/symbols', methods = ['GET'])
@cross_origin()
def symbols():
    if request.method == 'GET':
        import requests
        url = "https://free.currconv.com/api/v7/currencies?apiKey=4409081e6078be413a53"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text.encode('utf8'))


@app.route('/convert', methods = ['GET'])
@cross_origin()
def convert():
    if request.method == 'GET':
        import requests
        symbolFrom = request.args.get('from')
        symbolTo = request.args.get('to')

        url = "http://free.currconv.com/api/v7/convert?apiKey=4409081e6078be413a53&q={}_{}".format(symbolFrom,symbolTo)
        print(url)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text.encode('utf8'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)