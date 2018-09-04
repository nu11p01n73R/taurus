import re


key_map = {
        'Total Revenue': 'total_revenue',
        'Other Income': 'other_income',
        'Total Expenses': 'total_expense',
        'Depreciation And Amortisation Expenses': 'depreciation',
        'Finance Costs': 'finance_cost',
        'Profit/Loss After Tax And Before ExtraOrdinary Items': 'pat',
        'Total Shareholders Funds': 'total_equity',
        'Profit/Loss For The Period': 'total_profit',
        'Total Assets': 'total_assets',
        'Fixed Assets': 'total_fixed_assets',
        'Long Term Borrowings': 'long_term_debt',
        'Short Term Borrowings': 'short_term_debt',
        'Profit/Loss Before Tax': 'pbt',
        'Total Current Assets': 'current_assets',
        'Total Current Liabilities': 'current_liabilities',
        'Trade Receivables': 'trade_receivables'}


def normalize(value):
    return float(value.strip(' ').replace(',', ''))


def normalize_year(value):
    year_re = r'(?:Mar|Dec) \d\d'
    match = re.search(year_re, value.strip(' '))
    return value.strip(' ').strip('\r') if match else None


def extend(a_dict, first_key, second_key, value):
    has = a_dict.get(first_key, {})
    has[second_key] = value
    a_dict[first_key] = has
    return a_dict


def parse(data):
    output = {}
    years = []
    for line in data.split('\n'):
        pieces = line.split('\t')
        search = pieces[0].strip(' ')

        if not search and not years:
            years = [y for y in (normalize_year(x) for x in pieces[1:]) if y]

        if search in key_map:
            key = key_map[search]
            for i, value in enumerate(pieces[1:]):
                year = years[i]
                output = extend(output, year, key, normalize(value))

    return output
