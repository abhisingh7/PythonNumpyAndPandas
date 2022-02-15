import pandas as pd

# Similar to pivot_table(), melt() is used to transform or reshape data

# 1. Creating dataframe using csv
print("1. Creating dataframe using csv...\n")
df = pd.read_csv("weather.csv")
print(df)

# 2. using melt() method
print("\n2. using melt() method...\n")
df1 = pd.melt(df, id_vars=["day"])
print("New Dataframe: \n",df1)


# 3. filtering on melt dataframe
print("\n3. filtering on melt dataframe...\n")
print(df1[df1["variable"]=="chicago"])

# 4. To update column names
print("\n4. To update column names...\n")
df1 = pd.melt(df, id_vars=["day"], var_name="city", value_name="temperature")
print("\nUpdated columns Dataframe: \n",df1)