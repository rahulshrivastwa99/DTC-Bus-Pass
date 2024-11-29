from datetime import date
from dateutil.relativedelta import relativedelta

six_months = date.today() + relativedelta(months=+6)
present = date.today() + relativedelta(days=-5)
print(present)