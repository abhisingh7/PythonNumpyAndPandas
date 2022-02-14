import pandas as pd
import numpy as np

# 1. Creating data frame
print("1. Creating dataframe...\n")
df = pd.read_csv("weather_data.csv")
print(df)

# 2. Replacing a specific value (-99999) with NaN
print("\n2. Replacing a specific value (-99999) with NaN...\n")
new_df = df.replace(-99999,np.NaN)
print("New dataframe...\n",new_df)

# 3. Replacing a list of specific values (-99999,-88888) with NaN
print("\n3. Replacing a list of specific values (-99999,-88888) with NaN...\n")
new_df = df.replace([-99999,-88888],np.NaN)
print("New dataframe...\n",new_df)

# 4. Replacing values based on specific column
print("\n4. Replacing values based on specific column...\n")
new_df = df.replace({
    'temperature': -99999,
    'windspeed': [-99999,-88888],
    'event': '0'
    },np.NaN)
print("New dataframe...\n",new_df)

# 5. Replacing with multiple values
print("\n5. Replacing with multiple values...\n")
new_df = df.replace({
    -99999: np.NaN,
     "No Event": "Sunny"
    })
print("New dataframe...\n",new_df)

# 6. Replacing a specific column values using regex
df2 = pd.read_csv("weather_data2.csv")
print("\n6. Replacing a specific column values using regex...\n")
print("Dataframe: \n",df2)
new_df = df2.replace({
    'temperature': '[A-Za-z]',
    'windspeed': '[A-Za-z]'
    },'',regex=True)
print("\nNew dataframe...\n",new_df)

# 7. Replacing a list of values with another list of values
df = pd.DataFrame({
    'score':['exceptional', 'average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
    })
print("\n7. Replacing a list of values with another list of values...\n")
print("\nDataframe: \n",df)
new_df = df.replace(['poor', 'average', 'good', 'exceptional'],[1,2,3,4])
print("\nNew dataframe...\n",new_df)