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

# Close prices
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


# ----------------------------------------------------------------------------
#   Indexing using lists
# ----------------------------------------------------------------------------

# The `start` variable will hold the first index in the slice and the `end`
# variable will hold the last index in the slice. Remember that the `index`
# list method will return the position of the element in the list, starting at
# 0. In this case, `start` will be set to 2 and `end` will be set to 6.

# Remember to uncomment the statements below and complete the part with '?'
start = dates.index('2020-01-06')
end = dates.index('2020-01-10')
print(start, end)

# Now, slice the `prices` list.
# Remember that slices do not include endpoints
prcs_w1 = prices[start:end+1]

# Finally, calculate the average of the prices in the slice
avgprc = sum(prcs_w1)/len(prcs_w1)
print(avgprc)  