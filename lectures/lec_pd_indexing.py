""" lec_pd_indexing.py

Companion codes for the lecture on indexing pandas objects
"""

import pandas as pd

# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# Trading day counter
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

# ----------------------------------------------------------------------------
#   Create instances
# ----------------------------------------------------------------------------

# Create a series object
ser = pd.Series(data=prices, index=dates)
print(ser)

# Data Frame with close and Bday columns
df = pd.DataFrame(data={'Close': ser, 'Bday': bday}, index=dates)
print(df)

# 1.1 Series
# -------------

# 1.1.1 Series.loc: Selection using a single label
# ser.loc[label] --> scalar if label in index, error otherwise

# Set `x` below to be the price on 2020-01-10
x = ser.loc['2020-01-10'] # --> 7.0

# The following will raise a KeyError
#ser.loc['3000-01-10'] # --> KeyError


# Using .loc to set elements:
# Copy the series
ser2 = ser.copy()
print(ser2)



# Set the price for 2020-01-02 to zero
ser2.loc['2020-01-02'] = 0
print(ser2)

# 1.1.2 Series.loc: Selection using sequence of labels
# will return a series

x = ser.loc[['2020-01-03', '2020-01-10']]
print(x)


print(type(x)) # --> <class 'pandas.core.series.Series'>


# 1.1.3 Series.loc: Selection using slices
# (endpoints are included!)
# Similarly to selection with series, using slices also returns a series.
# Importantly, the endpoint is included when selecting with slices!

x = ser.loc['2020-01-03':'2020-01-10']
print(x)


# 1.2 DataFrames
# -------------

# 1.2.1 Selection using a single label:
# A single row and column labels will return a single value (scalar)

# For instance, selecting the close price on January 3, 2020
x = df.loc['2020-01-03', 'Close']
print(x) # --> 7.19

# A single row **or** a single column label will return a series:
# The following will return a series corresponding to the column "Close"
x = df.loc[:,'Close']
print(x)


type(df.loc[:,'Close']) # --> <class 'pandas.core.series.Series'>

y = df.loc['2020-01-03', :]
print(y)

print(type(df.loc['2020-01-03', :])) # --> <class 'pandas.core.series.Series'>

# When omitting column labels, pandas will return a series if the row label
# exists. Otherwise it will raise an exception

# This is equivalent to df.loc['2020-01-03',:]
x = df.loc['2020-01-03']
print(x)

print(type(df.loc['2020-01-03'])) # --> <class 'pandas.core.series.Series'>

# This will raise an exception because the label does not exist
#df.loc['2020-01-01']


# 1.2.2 Dataframe.loc: Selection using sequence of labels

# Set x so it contains the closing prices for '2020-01-02' and '2020-01-03'
x = df.loc[['2020-01-02', '2020-01-03'], 'Close']
print(x)


# 1.2.3 Dataframe.loc: Selection using slices
# Using slices will return
#  - A series if the other index is a single label
#  - A data frame otherwise


# the next statement is equivalent to x = df.loc['2020-01-01':'2020-01-10']
x = df.loc['2020-01-01':'2020-01-10', :]
print(x)

print(type(x)) # --> <class 'pandas.core.frame.DataFrame'>


some_list = [1, 2, 3, 4]

# Slices do not include endpoints
# x -> [1]
x = some_list[0:1]

# This will not raise an exception
# x -> []
x = some_list[100:101]

x = df.loc['2999-01-01':'2999-01-10', :]
print(x)


print(type(x)) # --> <class 'pandas.core.frame.DataFrame'>


# Slices can be open ended
# However, single row labels and open column slices will NOT return a
# data frame, they will return a series!!!

x = df.loc['2020-01-06':, :]
print(x)

x = df.loc['2020-01-06', 'Close':]
print(x)


print(type(x)) # --> <class 'pandas.core.series.Series'>

# Slices do not work as expected if the data is not sorted
# NOTE: don't worry about the rename method now

df2 = df.copy()

df2.rename(index={'2020-01-08':'1900-01-01'}, inplace=True)

print(df2)


x = df2.loc['2020-01-03':'2020-01-10', :]
print(x)


# You can avoid these issues by sorting the dataframe first
df2.sort_index(inplace=True)
x = df2.loc['2020-01-03':'2020-01-10', :]
print(x)



# This will return a DataFrame
x = df.loc['2020-01-03':'2020-01-03']
print(x)



# This will return a series
x = df.loc['2020-01-03']
print(x)


print(type(x)) # -->  <class 'pandas.core.series.Series'>


# 2.1 Series
# -------------

# 2.1.1 Series.iloc: Selection using a single label
# Series.iloc using single index will return a numpy scalar

# ser.iloc[pos] --> scalar if abs(pos) < len(ser), otherwise error
x = ser.iloc[0]  # --> 7.16
x = ser.iloc[-1] # --> 7.04

#x = ser.iloc[100] # raises IndexError

# Using .loc for assignment
# Copy the series
s2 = ser.copy()

# assign
s2.iloc[0] = 0
print(s2)


# 2.1.2 Series.iloc: Selection using sequence of labels

x = ser.iloc[[0, 2]]
print(x)


# 2.1.3 Series.iloc: Selection using slices
# Slices will not include endpoints, otherwise, work like ser.loc

x = ser.iloc[0:1] # x --> series with one row
print(x)



x = ser.iloc[0:2]
print(x)


# 2.2 Dataframe
# -------------

# 2.2.1 Dataframe.iloc: Selection using a single label

# df.iloc[row pos] --> series if abs(pos) < len(df.index)
# --> series with elements from the first "row" -- column labels as row indexes

x = df.iloc[0]
print(x)


# Equivalent to
x = df.iloc[0,:]
print(x)




# First column (and all rows):
x = df.iloc[:,0]
print(x)


# This will return a series with the first two columns as labels:
x = df.iloc[0,[0,1]]
print(x)


# This will return a *dataframe* with the first row of df
x = df.iloc[0:1,:]
print(x)


# print(type(x)) # --> <class 'pandas.core.frame.DataFrame'>

# If the column indexer is omitted, all columns will be returned.

# df.iloc[list of row pos] --> dataframe with rows in the list
# Note: will raise IndexError if pos is out of bounds
x = df.iloc[[0, 1]] # --> DF with first two rows of df
print(x)

# The following will raise an exception
#x = df.iloc[[0, 10]] # --> raises IndexError

# The following will raise an exception
#x = df.iloc[[0,100], :]

x = df.iloc[1:1000, :]
print(x)

x = df.iloc[999:1000, :]
print(x)

# Slices can be open ended
x = df.iloc[2:, :]
print(x)


x = df.iloc[0, 0:]
print(x)


# This will return an empty series
x = df.iloc[0, 10:]
print(x)



print(ser)


# 3.1.1 label, list of labels, label slices

# Set `x` to be the price for '2020-01-13'
x = ser['2020-01-13']
print(x) # --> 7.02

# The following raises KeyError because label not part of ser.index
#x = ser['3000-01-10']

# Set `x` to be a series with the first two rows of `ser`
x = ser[['2020-01-02', '2020-01-03']] # --> first two rows

# All labels must exist
#x = ser[['2020-01-02', '3000-01-10']] # raises KeyError because a label is not part of ser.index


# Set `x` to include all obs between  '2020-01-13' and '2020-01-14'
x = ser['2020-01-13':'2020-01-14']
print(x)


# The `ser` above is sorted by index.
# Set `x` to include all obs between '2020-01-13' and '3000-01-01'. The
# end data (obviously) is not part of the series
x = ser['2020-01-13':'3000-01-01']
print(x)



# Create a series with an unsorted index
new_ser = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])

# First, select a slice from 'a' to 'b'. Because both labels are included in
# the index, the slice will contain all obs between the indexes 'a' and 'b'
x = new_ser['a':'b']
print(x)

# Next, select a slice from 'b' to 'z'. Note that 'z' is not part of the
# index. Since the index is not sorted, the following will result in an error
#x = new_ser['b':'z']

# Series also have a method called `sort_index`, which will return a copy of the
# series with sorted indexes:


# Sort the series
sorted_ser = new_ser.sort_index()
print(sorted_ser)


# This will return only the first rows (not the entire series as before)
x = sorted_ser['a':'b']
print(x)



# `sorted_ser` is sorted so the following will return the intersection between
# the slice and the row labels
x = sorted_ser['b':'z']
print(x)


# 3.1.2 position, list of positions, position slices

# Using the ser created above
print(ser)


# Get the first element of the series
#x = ser[0]

# Get the first and fourth element (series)
#x = ser[[0,3]]

# NOTE: When using slices, the endpoints are NOT included
# This will return a series with the first element only
x = ser[0:1]
print(x)


# This will return the first five elements of the series
x = ser[:5]
print(x)


# This will return every other element, starting at position 0
x = ser[::2]


# This returns the series in reverse order
x = ser[::-1]



new_ser = pd.Series(data=['a','b', 'c'], index=[1, -4, 10])
# This will produce an empty series (because pandas thinks these are positions, not labels)
x = new_ser[1:-4]
print(x)


print(df)



# df[column label] --> series if column exists, error otherwise
# `x` will be a series with values in Close
x = df['Close']
print(x)
# Returns a series:


print(type(df["Close"]))
# <class 'pandas.core.series.Series'>

# Note that the label is case sensitive. For instance the following
# raises KeyError
#df['CLOSE']


# Sequences of labels
# df[list of column labels] --> dataframe with columns in the same order
# as the column labels
# Note: All column labels must exist, otherwise error
cols = ['Close', 'Bday']
print(df[cols])

print(df[["Close", "Bday"]])

print(type(df[["Close", "Bday"]]))



# 3.2.2 row label slices
# ----------------------------------------------

# Slices work similar to ser[slice], i.e., they operate on row indexes
# `x` will be an empty datafame because the slice is not part of the row
# labels
x = df['Close': 'Bday']
print(x)



# Slicing DFs with [] works very differently than one would expect:
# x --> dataframe with first two rows
x = df['2020-01-02':'2020-01-03']
print(x)



# You can use position instead of row labels, but endpoints are NOT included
# x --> all rows but the last one
x = df[:-1]
print(x)

# Will NOT raise error if out of bounds
# x -> returns empty DF
x = df[100:1001]
print(x)
# Returns:
# Empty DataFrame
# Columns: [Close, Bday]
# Index: []

