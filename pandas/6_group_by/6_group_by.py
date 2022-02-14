import pandas as pd

# 1. Creating dataframe
print("1. Creating dataframe...\n")
df = pd.read_csv("weather_by_cities.csv")
print(df)

# 2. Grouping data
print("\n2.Grouping data...\n")
g = df.groupby('city')
print(g)
print()
for city, city_df in g:
    print(city)
    print(city_df)

# 3. Accessing an specific group
print("\n3. Accessing an specific group...\n")
print(g.get_group('mumbai'))

# 4. getting maximum data for each city
print("\n4. Getting maximum data for each city...\n")
print(g.max())

# 5. getting mean or Average data for each city
print("\n5. getting mean or Average data for each city...\n")
print(g.mean())

# 6. Get all analysis in one shot
print("\n6. Get all analysis in one shot...\n")
print(g.describe()) # In jupyter notebook it shows result in good format

# Use in Jupyter notebook to plot charts
# %matplotlib inline
# g.plot()