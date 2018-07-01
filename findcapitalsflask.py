#!/usr/bin/python3
#coding: utf-8
from countrycapitals import countrycapitalsdict
from flask import Flask, jsonify, make_response


app = Flask(__name__)


@app.route('/api/<string:countryname>', methods=['GET'])
def findcountrycapital(countryname):
    countryname=countryname.title() #capitalize first chars to match data format
    if len(countryname) == 0:
        abort("404")
    else:
        try:
            capital = countrycapitalsdict[countryname]
        except KeyError: #country not found in dict
            return jsonify({"error": "Not found"})
    return jsonify({"country":countryname,"capital": capital})


#handle errors(wrong route, empty query)
@app.errorhandler(404)
def notfound(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(debug=True)
