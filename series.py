# https://wikidocs.net/4364
# What is Pandas?
# Pandas is one of the most commonly used libraries for analysing data
# Series: One-dimensional ndarray with axis labels
from pandas import Series

kakao = Series([45000, 46000, 45500, 45400, 45600])
print(kakao)
print(kakao[1])
print(kakao[3])

# unlike Python's list, we can assign our indexes to values in Pandas' Series
naver = Series([50000, 60000, 40000, 70000, 80000], index=['2022-02-01', '2022-02-02', '2022-02-03', '2022-02-04', '2022-02-05'])
print(naver)
print(naver['2022-02-01'])
print(naver['2022-02-02'])

# it prints out all the indexes stored in naver
for date in naver.index:
    print(date)
# it prints out all the values stored in naver
for price in naver.values:
    print(price)

# pandas' series automatically match values that have same index
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merged = mine + friend
print(merged)