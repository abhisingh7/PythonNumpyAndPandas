import pandas as pd

# 1. Creating dataframe
print("1. Creating dataframe...\n")
df = pd.read_excel("stocks.xlsx", header=[0,1])
print(df)

# 2. stacking columns
# it will do stacking on the basis of innermost header
print("\n2. stacking columns...\n")
print(df.stack()) # looks good in jupyter nb

# 3. taking first row header into stacking
print("\n3. taking first row header into stacking...\n")
print(df.stack(level=0))

# 4. unstacking dataframe
print("\n4. unstacking dataframe...\n")
df_stacked = df.stack()
print("stacked df: \n",df_stacked)
print("Unstacked df: \n",df_stacked.unstack()) # looks good in jupyter nb

# 5. creatind dataframe of 3 level header excel
print("\n5. creatind dataframe of 3 level header excel...\n")
df2 = pd.read_excel("stocks_3_levels.xlsx", header= [0,1,2])
print(df2)

# 6. stacking dataframe
# by default take innermost level header
print("\n6. stacking dataframe...\n")
print(df2.stack())