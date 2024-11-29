from flask import Flask, render_template
app = Flask(__name__)

from datetime import date
from dateutil.relativedelta import relativedelta

six_months = date.today() + relativedelta(months=+6)
present = date.today() + relativedelta(days=-4)

@app.route('/')
def hello_world():
    end_year = six_months.year
    end_month = six_months.month
    end_day = six_months.day-3
    start_year = present.year
    start_month = present.month
    start_day = present.day
    return render_template("index.html", end_year=end_year,end_month=end_month,end_day=end_day, start_day=start_day,start_month=start_month,start_year=start_year)



if __name__ == "__main__":
    app.run(debug=True)
