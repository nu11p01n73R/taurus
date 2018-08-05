def get_operating_revenue(data):
    return data['total_revenue'] - data['other_income']


def get_operating_expense(data):
    return data['total_expense'] - data['finance_cost'] - data['depreciation']


def get_ebitda_margin(data):
    operating_revenue = get_operating_revenue(data)
    operating_expense = get_operating_expense(data)
    return ((operating_revenue - operating_expense)
            / operating_revenue * 100)


def get_pat_margin(data):
    return data['pat'] / data['total_revenue'] * 100


def get_roe(data):
    return data['pat'] / data['total_equity'] * 100


def get_roa(data):
    return ((data['pat'] + data['finance_cost'] * (1 - 32))
            / data['total_assets'] * 100)


def get_total_debt(data):
    return data['short_term_debt'] + data['long_term_debt']


def get_roce(data):
    overall_capital = data['total_equity'] + get_total_debt(data)
    return data['pbt'] / overall_capital * 100


def get_interest_coverage(data):
    ebitda = get_operating_revenue(data) - get_operating_expense(data)
    return ebitda / data['finance_cost']


def get_debt_to_equity(data):
    total_debt = get_total_debt(data)
    return total_debt / data['total_equity']


def get_debt_to_asset(data):
    return get_total_debt(data) / data['total_assets'] * 100


def get_financial_leverage(data):
    return data['total_assets'] / data['total_equity']


def get_fixed_asset_turnover(data):
    return get_operating_revenue(data) / data['total_fixed_assets']


def get_working_capital(data):
    return data['current_assets'] - data['current_liabilities']


def get_working_capital_turnover(data):
    return get_operating_revenue(data) / get_working_capital(data)


def get_inventory_turnover(data):
    pass


def get_receivable_turnover(data):
    return get_operating_revenue(data) / data['trade_receivables']


def analyze_per_year(data):
    method_map = {
            'ebitda_margin': get_ebitda_margin,
            'pat_margin': get_pat_margin,
            'roe': get_roe,
            'roa': get_roa,
            'roce': get_roce,
            'interest_coverage': get_interest_coverage,
            'debt_to_equity': get_debt_to_equity,
            'debt_to_asset': get_debt_to_asset,
            'financial_leverage': get_financial_leverage,
            'fixed_asset_turnover': get_fixed_asset_turnover,
            'working_capital': get_working_capital,
            'working_capital_turnover': get_working_capital_turnover,
            'receivable_turnover': get_receivable_turnover}

    output = {}
    for key, method in method_map.items():
        output[key] = method(data)

    return output


def analyze(data):
    output = {}
    for year, year_data in data.items():
        output[year] = analyze_per_year(year_data)

    return output
