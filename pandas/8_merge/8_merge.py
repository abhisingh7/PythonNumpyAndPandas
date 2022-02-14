import pandas as pd

# 1. Creating homogeneous dataframe
print("\n1. Creating homogeneous dataframe\n")
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
print("Temperature_df: \n", df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
print("\nhumidity_df: \n",df2)

# 2. Merging dataframe for homogeneous dataframes (inner join or intersection of both dataframe)
print("\n2. Merging dataframe for homogeneous dataframes "
      "(inner join or intersection of both dataframe)...\n")
df3 = pd.merge(df1,df2, on="city")
print("Merged df: \n",df3)

# 3. Creating heterogeneous dataframe
print("\n3. Creating heterogeneous dataframe\n")
df4 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "Baltimore"],
    "temperature": [21,14,35,32],
})
print("Temperature_df: \n", df4)

df5 = pd.DataFrame({
    "city": ["chicago","new york","san francisco"],
    "humidity": [65,68,71],
})
print("\nhumidity_df: \n",df5)

# 4. Merging dataframe for heterogeneous dataframes (inner join or intersection of both dataframe)
print("\n4. Merging dataframe for heterogeneous dataframes ("
      "inner join or intersection of both dataframe)...\n")
df6 = pd.merge(df4,df5, on="city")
print("Merged df: \n",df6)

# 5. Merging dataframe for heterogeneous dataframes (Outer join or union of both dataframe)
print("\n5. Merging dataframe for heterogeneous dataframes "
      "(Outer join or union of both dataframe)...\n")
df6 = pd.merge(df4,df5, on="city", how="outer", indicator=True) # By default how="inner"
# indicator argument is used to check from which dataframe the results are coming.
print("Merged df: \n",df6)

# 6. Merging dataframe using left join
print("\n6. Merging dataframe using left join ...\n")
df6 = pd.merge(df4,df5, on="city", how="left") # By default how="inner"
print("Merged df: \n",df6)

# 7. Merging dataframe using right join
print("\n6. Merging dataframe using right join ...\n")
df6 = pd.merge(df4,df5, on="city", how="right") # By default how="inner"
print("Merged df: \n",df6)

# 8. Suffixes
print("\n8. Suffixes...\n")
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})
print(df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
print("\n",df2)

df3= pd.merge(df1,df2,on="city")
print("\ndataframe merged without using suffix:\n",df3)

df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
print("\ndataframe merged with using suffix:\n",df3)
