import sys
from pprint import pprint
from parser import parse
from analyzer import analyze


file_name = sys.argv[1]
with open(file_name) as data_file:
    data = data_file.read()
    parsed_data = parse(data)
    ratios = analyze(parsed_data)
    pprint(parsed_data)
    print("=====================")
    pprint(ratios)
