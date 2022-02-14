import pandas as pd

# 1. Creating India weather dataframe
print("1. Creating India weather dataframe...\n")
india_weather = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32,45,30],
    "humidity": [80,60,78]
})
print(india_weather)

# 2. Creating USA weather dataframe
print("\n2. Creating USA weather dataframe...\n")
us_weather = pd.DataFrame({
    "city": ["new york", "chicago", "orlando"],
    "temperature": [21,14,35],
    "humidity": [68,65,75]
})
print(us_weather)

# 3. Join both dataframe
print("\n3. Join both dataframe...\n")
df = pd.concat([india_weather,us_weather]) # Can join multiple no. of dataframes
print(df)

    # Since index are also concating, we want continuous indexing
print("\n fixing indexing \n")
df = pd.concat([india_weather,us_weather], ignore_index=True) # Can join multiple no. of dataframes
print(df)

# 4. Attaching keys to our dataframes
# Note:cannot use ignore_index in argument otherwise it won't work
print("\n4. Attaching keys to our dataframes...\n")
df = pd.concat([india_weather,us_weather], keys=["india", "us"])
print(df)
print("\nGetting a subset of dataframe: \n",df.loc["india"])

# 5. Append dataframe as column instead of rows
print("\n5. Append another dataframe as column instead of rows...\n")
temperature_df = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32,45,30]
})
print("Temperature Dataframe: \n", temperature_df)
windspeed_df = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "windspeed": [7,12,9]
})
print("\n Windspeed Dataframe: \n", windspeed_df)

df = pd.concat([temperature_df, windspeed_df], axis=1) # by default axis=0(rows)
print("\nConcating df as columns: \n",df)

# 6. Append dataframe as column using indexing if data is mismatching

# Note: we are doing indexing in our dataframe
# so data should be shown for same city in a row while appending

print("\n6. Append dataframe as column using indexing if data is mismatching...\n")
temperature_df = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32,45,30]
}, index = [0,1,2])
print("Temperature Dataframe: \n", temperature_df)
windspeed_df = pd.DataFrame({
    "city": ["delhi", "mumbai"],
    "windspeed": [7,12]
}, index = [1,0])
print("\n Windspeed Dataframe: \n", windspeed_df)

df = pd.concat([temperature_df, windspeed_df], axis=1) # by default axis=0(rows)
print("\nConcating df as columns using indexing: \n",df)

# 7. Append dataframe with series

print("\n7. Append dataframe with series...\n")
temperature_df = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32,45,30]
}, index = [0,1,2])
print("Temperature Dataframe: \n", temperature_df)

s = pd.Series(["Humid", "Dry", "Rain"], name="event")
print("\n Series: \n",s)
df = pd.concat([temperature_df, s], axis=1) # by default axis=0(rows)
print("\nConcating df columnwise with a series : \n",df)