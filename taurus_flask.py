from flask import Flask, jsonify, abort, request
from stock import Stock
from parser import parse
from pprint import pprint


app = Flask('taurus')


@app.errorhandler(404)
def not_found(error):
    response = {'code': 404, 'message': 'Not Found'}
    return jsonify(response)


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/stocks')
def get_all_stocks():
    stocks = Stock.find_all()
    return jsonify([stock.toJson() for stock in stocks])


@app.route('/stocks/<sid>')
def get_stock(sid):
    stock = Stock.find(sid)

    if stock:
        return jsonify(stock.toJson())
    else:
        abort(404)


@app.route('/stocks', methods=['POST'])
def create_stock():
    name = request.form['stock_name']
    sid = request.form['stock_id']

    stock = Stock(sid, name)

    data = request.form['data']
    parsed_data = parse(data)
    pprint(parsed_data)

    stock.set_data(parsed_data)
    stock.analyze()
    stock.save()

    return jsonify(stock.toJson())


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
