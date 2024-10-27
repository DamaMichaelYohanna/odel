from datetime import datetime
import pandas as pd
start = datetime(1978, 4, 10).strftime("%m/%d/%Y")

end = datetime(2024, 5, 1).strftime("%m/%d/%Y")

ff = list(pd.date_range(start=start, end=end, periods =4 ).year)
print(ff)