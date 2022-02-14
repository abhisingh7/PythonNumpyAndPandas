import pandas as pd

# 1. Creating dataframe using weather.csv
print("1. Creating dataframe using weather.csv...\n")
df = pd.read_csv("weather.csv")
print(df)

# 2. creating pivot for weather df using pivot() method
# Note: pivot() is used to change axis of dataframe according to our need.
print("\n2. Creating pivot table for weather df using pivot() method...\n")
print(df.pivot(index="date", columns="city"))

# 3. Getting specific columns
print("\n3. Getting specific columns...\n")
print(df.pivot(index="date", columns="city", values="humidity"))

# 4. Creating dataframe using weather2.csv
#Note: pivot_table() is used to summarize and aggregate data inside dataframe
# in weather2.csv we have two values for same date for a single city. we would like to see avg.
print("\n4. Creating dataframe using weather2.csv...\n")
df = pd.read_csv("weather2.csv")
print(df)

# 5. creating pivot table for weather2 df using pivot_table()
print("\n5. Creating pivot table for weather2 df to get average using pivot_table()...\n")
print(df.pivot_table(index="city", columns="date")) # by default , aggfunc="mean"

# 6. creating pivot table for weather2 df and getting sum using aggfunc flag
print("\n6. Creating pivot table for weather2 df to get sum usig aggfunc flag ...\n")
print(df.pivot_table(index="city", columns="date", aggfunc="sum")) # by default , aggfunc="mean"

    # we can use aggfunc= "diff" or "count" etc. various different aggregating function.


# 7. Using margins flag, to get avg. on axis = 0(rows) and axis = 1(columns)
print("\n7. Using margins flag, to get avg. on axis = 0(rows) and axis = 1(columns) ...\n")
print(df.pivot_table(index="city", columns="date", margins=True))


# 8. Creating weather3.csv dataframe
print("\n8. Creating weather3.csv dataframe...\n")
df = pd.read_csv("weather3.csv")
print(df)

# 9. Use Grouper() method for aggregation
# It will give average.
print("\n9. Use Grouper() method for aggregation...\n")
df['date'] = pd.to_datetime(df['date']) # Changing datatype to date(timestamp) from str
print(df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city'))
