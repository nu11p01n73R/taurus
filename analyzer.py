def get_ebitda_margin(data):
    operating_revenue = data['total_revenue'] - data['other_income']
    operating_expense = data['total_expense'] - data['finance_cost']
    return ((operating_revenue - operating_expense)
            / operating_revenue * 100)


def get_pat_margin(data):
    return data['pat'] / data['total_revenue'] * 100


def get_roe(data):
    return data['pat'] / data['total_equity'] * 100


def get_roa(data):
    return ((data['pat'] + data['finance_cost'] * (1 - 32))
            / data['total_assets'] * 100)


def get_roce(data):
    overall_capital = (data['total_equity'] +
                       data['short_term_debt'] +
                       data['long_term_debt'])
    return data['pbt'] / overall_capital * 100


def analyze_per_year(data):
    method_map = {
            'ebitda_margin': get_ebitda_margin,
            'pat_margin': get_pat_margin,
            'roe': get_roe,
            'roa': get_roa,
            'roce': get_roce}

    output = {}
    for key, method in method_map.items():
        output[key] = method(data)

    return output


def analyze(data):
    output = {}
    for year, year_data in data.items():
        output[year] = analyze_per_year(year_data)

    return output
