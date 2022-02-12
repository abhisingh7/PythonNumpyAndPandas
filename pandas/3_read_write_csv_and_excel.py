import pandas as pd

# 1. Read CSV
print("1. Creating dataframe from csv file...\n")
df = pd.read_csv("..\\files\\stock_data.csv")
print(df)

# 2. sometimes we have an extra row above our columns in csv, we can skip that row from our df
print("\n2. Creating dataframe by skipping few rows to get a good header\n")
df = pd.read_csv("..\\files\\stock_data2.csv", skiprows=1)
# df = pd.read_csv("..\\files\\stock_data2.csv", header=1) # Both skiprows and header works same
print(df)

# 3. sometimes we don't have header in our csv
print("\n3. sometimes we don't have header in our csv, so we are creating one\n")
df = pd.read_csv("..\\files\\stock_data3.csv", header=None,
                 names=['ticker','eps','revenue', 'price', 'people'])
print(df)

# 4. Creating dataframe of selected rows instead of whole csv data
print("\n4. Creating dataframe of selected rows instead of whole csv data...\n")
df = pd.read_csv("..\\files\\stock_data.csv", nrows=3)
print(df)

# 5. Clean up messy data. Turning not available values into NaN
print("\n5. Turning not available values into NaN...\n")
df = pd.read_csv("..\\files\\stock_data.csv", na_values=["not available","n.a."])
print(df)

# 6. Another way of cleaning up
print("\n6. Another way of cleaning up...\n")
df = pd.read_csv("..\\files\\stock_data.csv", na_values={
    'eps': ["not available", "n.a."],
    'revenue': ["not available", "n.a.", -1],
    'people': ["not available", "n.a."],
    'price':["not available", "n.a.",-1]
    })
print(df)

# 7. Write to csv from dataframe
print("\n 7. Write back to csv from dataframe...\n")
# df.to_csv('..\\files\\new.csv') # Mention path to save csv
    # by default it creates index. to remove index from csv...
df.to_csv('..\\files\\new.csv', index=False)
print("CSV File saved on mentioned location. Check it!!")

# 8. creating column specific csv.
print("\n 8. creating column specific csv...\n")
print(df.columns)
    # we are creating csv with only these two columns from df.
df.to_csv('..\\files\\new.csv', index=False, columns=['tickers','eps'])
print("CSV File saved on mentioned location. Check it!!")

# 9. creating column specific csv and removing header.
print("\n 9. creating column specific csv and removing header...\n")
    # we are creating csv with only these two columns from df and removing columns.
df.to_csv('..\\files\\new.csv', index=False, columns=['tickers','eps'], header=False)
print("CSV File saved on mentioned location. Check it!!")


print("\n##############################################################")

# 10. Read excel
print("10. Creating dataframe from excel file...\n")
df = pd.read_excel("..\\files\\stock_data.xlsx", "sheet1")
print(df)

# 11. Reading excel and creating df by converting specific cells in a column
# to some different values
print("\n11. converting specific cells in a column to some different values\n")
print("\n Current dataframe is : \n", df)

    # we want to convert n.a. from people column to 'sam walton'.
def convert_people_cell(cell):
    if cell == "n.a.":
        return 'sam walton'
    return cell

def convert_eps_cell(cell):
    if cell == "not available":
        return None
    return cell
df = pd.read_excel("..\\files\\stock_data.xlsx", "sheet1", converters={
    'people': convert_people_cell,
    'eps': convert_eps_cell
    })
print("\n df after using converters: \n",df)

# 12. Creating excel from dataframe
print("\n 12. Write back to excel from dataframe...\n")
df.to_excel("..\\files\\new.xlsx", sheet_name="stocks")
print("Excel File saved on mentioned location. Check it!!")

# 13. shifting start position of excel file to specific row and column
print("\n 13. shifting start position of excel file to specific row and column...\n")
df.to_excel("..\\files\\new.xlsx", sheet_name="stocks", startrow=1, startcol=2, index=False)
print("Excel File saved on mentioned location. Check it!!")

# 14. Creating excel workbook having two sheets from two dataframes
print("\n14. Creating excel workbook from two dataframes\n")
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845,65,64],
    'pe': [30.37,14.26,30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather = pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter('..\\files\\stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")

print("Excel workbook created. Check It!!")