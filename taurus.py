import sys
from parser import parse
from stock import Stock


if len(sys.argv) != 4:
    msg = '''Error: Missing data file

Usage:
    taurus.py stock_id stock_name file_name'''
    print(msg)
    sys.exit(1)

sid = sys.argv[1]
name = sys.argv[2]
file_name = sys.argv[3]

stock = Stock(sid, name)
with open(file_name) as data_file:
    data = data_file.read()
    parsed_data = parse(data)

    stock.set_data(parsed_data)
    stock.analyze()

    stock.save()
    stock.print()
