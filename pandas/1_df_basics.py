import pandas as pd

# 1. Creating data frame by reading csv file
print("1. Creating data frame by reading csv file...\n")
    # If file is in different location, mention full path
df = pd.read_csv("..\\files\\weather_data.csv")
print(df)
print()
# 2. Creating data frame via python dictionary
print("2. Creating data frame via python dictionary...\n")
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain','Sunny']
}
df = pd.DataFrame(weather_data)
print(df)
print("Dimension of dataframe: ", df.shape) #df.shape is a tuple so we can unpack it

rows, columns = df.shape
print("Rows: ",rows)
print("Columns", columns)

    # df.head() to print initial few rows. we can mention no. of rows to print
print("\nDF Head: \n",df.head())
print("\nDF Head: \n",df.head(2))

    # Like df.head(), we have df.tail to print last few rows of dataframe
print("\nDF Tail: \n",df.tail())
print("\nDF Tail: \n",df.tail(2))

# 3. Indexing and slicing in dataframe
print("3. Indexing and slicing in dataframe...\n")

print("\nDF Slicing by rows: \n",df[2:5])

# 4. Operations on columns
print("\n4. Operations on columns...\n")
    # printing columns
print("\n printing DF columns: \n")
print(df.columns)

    # printing individual column
print("\n printing individual column: \n")
print("printing column = day: \n", df.day) # df['day'] is also valid
print("\nprinting column = event: \n", df['event'])

    # type of column
print("\n Type of df column = event: \n",type(df['event']))

    # printing specific columns
print("\nprinting specific columns:\n", df[['event', 'day', 'temperature']])

# 5. Operations on dataframe
print("\n5. Operations on Dataframe...\n")

    # max(), min(), mean(), standard deviation,
print("\nMaximum Temperature: \n", df['temperature'].max())
print("\nMinimum Temperature: \n", df['temperature'].min())
print("\nMean of Temperature: \n", df['temperature'].mean())
print("\nStandard deviation of Temperature: \n", df['temperature'].std())

    # use describe method to get min, max, count,mean,std etc. in one call
print("\nDescribing dataframe: \n", df.describe())

# 6. Conditional operation on dataframe
print("\n6. Conditional operation on dataframe...\n")

print("\nGet rows where temperature >= 32:\n",df[df.temperature>=32]) #df[df['temperature'] >=32]

print("\nGet rows where temperature = maximum temp:\n",
      df[df['temperature']== df['temperature'].max()])

print("\nGet day and temperature columns only where temperature = maximum temp:\n",
      df[['day', 'temperature']][df['temperature']== df['temperature'].max()])


# 6. Setting index
print("\n6. Setting index...\n")
    # pandas automatically give index to each row from 0 to rows-1.
print("\n",df)
print("\nIndex range of dataframe:\n", df.index)

    # now set day column as index
print("\n setting day as index of df:\n", df.set_index('day'))

    # in above way it returns a new dataframe, not update original.
    # to update original dataframe use inplace argument in set_index()
print("\n setting day as index of df:\n", df.set_index('day', inplace=True))
# Now it will return none because it is doing modification instead of returning dataframe

print("printing updated dataframe:\n", df)

    # to get particular row on the basis of index(in our case it is day)

print("\n Using loc to get a particular row on the basis of index:\n",df.loc['1/3/2017'])

# 7. Resetting index
print("\n7. Resetting index...\n")

    # to reset index
df.reset_index(inplace=True)
print(df)

    # lets use 'event as index to check whether index can be duplicate or not.
print("\n now setting event as index to check duplicates allow in index or not...\n")
df.set_index('event', inplace=True)

print("\n Updated event index dataframe...\n", df)
print(df.loc['Snow']) # will return two rows, ideally should return one row for each index.

# Note: we can see that duplicates are allowed in indexing but we should avoid it because it will affect dataframe performance while doing operations on dataframe.