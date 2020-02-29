from flask import Flask, render_template, session, url_for, redirect, flash, request
import simplejson as json

app = Flask(__name__)

@app.route('/symbols', methods = ['GET'])
def symbols():
    import requests
    if request.method == 'GET':
        url = "http://data.fixer.io/api/symbols?access_key=471edf9bc157d6741d4bb23b556de379"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text.encode('utf8'))
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)