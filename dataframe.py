# https://wikidocs.net/4367
# DataFrame: Two-dimensional, size-mutable, potentially heterogeneous tabular data.

from pandas import DataFrame

raw_data = {'col0': [1,2,3,4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)


naver = {'open':  [11650, 11100, 11200, 11100, 11000],
         'high':  [12100, 11800, 11200, 11100, 11150],
         'low':  [11600, 11050, 10900, 10950, 10900],
         'close': [11900, 11600, 11000, 11100, 11050]}

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']

naver_day = DataFrame(naver, columns=['open', 'high', 'low', 'close'], index=date)
print(naver_day)


