import pandas as pd

# 1. Creating dataframe using csv
print("\n1. Creating dataframe using csv...\n")
df = pd.read_csv("weather_data.csv")
print(df)

# 2. Creating dataframe using excel file
print("\n2. Creating dataframe using excel file...\n")
df = pd.read_excel("weather_data.xlsx","sheet1")
print(df)

# 3. Creating dataframe using python dictionary
print("\n3. Creating dataframe using python dictionary...\n")
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain','Sunny']
}
df = pd.DataFrame(weather_data)
print(df)

# 4. Creating dataframe using tuples list
print("\n4. Creating dataframe using tuples list...\n")
weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow'),
]
df = pd.DataFrame(weather_data, columns=["day", "temperature", "windspeed", "event"])
print(df)

# 5. Creating dataframe using list of dictionaries
print("\n5. Creating dataframe using list of dictionaries...\n")
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'}
]
df = pd.DataFrame(weather_data)
print(df)

# There are more ways to create dataframe. To know more go to this link...
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html