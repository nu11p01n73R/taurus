from flask import Flask, jsonify, abort
from stock import Stock


app = Flask('taurus')


@app.errorhandler(404)
def not_found(error):
    response = {'code': 404, 'message': 'Not Found'}
    return jsonify(response)


@app.route('/stock/<sid>')
def get_stock(sid):
    stock = Stock.find(sid)

    if stock:
        return jsonify(stock.toJson())
    else:
        abort(404)
