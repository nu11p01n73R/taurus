# Taurus

Do fundamental analysis on companies with ease.


The [Moneycontrol]() website has good data about the various companies in
BSE and NSE. Taurus will help to do fundamental analysis on the data.

List of ratios currently supported,

- Debt To Asset
- Debt To Equity
- EBITDA Margin
- Financial Leverage
- Fixed Asset Turnover
- Interest Coverage
- PAT Margin
- Receivable Turnover
- ROA
- ROCE
- ROE
- Working Capital
- Working Capital Turnover


# Installation

The dependecies for this project are managed using [`pipenv`]
Clone the project and run,

```
pipenv install
```

The ratios calculated are saved in MongoDB.
The connection parameters to MongoDB can be configured using
the `config.ini` file or set as environment params,

```
MONGO_URL
MONGO_DB
```

# Usage

The taurus can be run using a cli script, `taurus.py` or 
using flask as web app.

To run as cli, head over to Moneycontrol and get the financial
data for the company(Balance Sheet and Profit and Loss). Paste
the data in a file and run script with the file as params.

```
pipenv python taurus.py data_file
```

To run the web app, run the below commands.

```
export FLASK_APP=taurus_flask.py
flask run
```
