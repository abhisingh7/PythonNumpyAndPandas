import pandas as pd

# 1. Converting day column into date type
print("\n1. Converting day column into date type...\n")
df = pd.read_csv("weather_info.csv")
print(df)
print("\n type of day column:", type(df.day[0]))

    # converting datatype of day column values from str to timestamp
print("\nconverting datatype of day column values from str to timestamp...\n")
df = pd.read_csv("weather_info.csv", parse_dates=["day"])
print(df)
print("\n type of day column:", type(df.day[0]))

    # setting day as index
print("\n setting day as index...\n")
df.set_index('day', inplace=True)
print("\n Updated dataframe: \n", df)

# 2. replace na values to some other values (we are replacing with 0)
print("\n2. replace na values to some other values (we are replacing with 0)....\n")
new_df = df.fillna(0) # Anywhere in our dataframe has NaN values will replaced by 0
print(new_df)

    # replacing na values for specific columns not for whole dataframe
print("\nreplacing na values for specific columns not for whole dataframe\n")
new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': "no event"
    })
print(new_df)
    # Note: Although we replace with 0. But this will not be looking good
    # if we take mean (avg) or std div. So we can follow the below approach

# 3. Replacing na value in whole dataframe with previous value
print("\n3.Replacing na value in whole dataframe with previous value\n")
new_df = df.fillna(method="ffill") # ffill = forward fill
print(new_df)

    # like forward fill (ffill) method ,
    # we have backward fill (bfill) method to carry forward next value
print("\nReplacing na value in whole dataframe with next value\n")
new_df = df.fillna(method="bfill") # bfill = backward fill
print(new_df)

    #fillna method has a parameter called axis
print("\nReplacing na value in whole dataframe with next value using axis in argument of fillna\n")
new_df = df.fillna(method="bfill", axis = "columns")
print(new_df)
    # Note : You can see that without using axis we were filling data on row basis(vertically)
    # but by using axis = "columns" , the next column value is filled in the previous column

    # fillna has a parameter called limit in which we can mention for how many rows
    # the ffill or bfill can work.
print("\nusing limit in fillna\n")
new_df = df.fillna(method="ffill", limit=1)
print(new_df)

# 4. interploate method. It is used to replace blank data on the previous and next value
# w.r.t. that cell. It is good for guessing or estimating values.
# By default, interpolate is linear that we can change using method= in parameter
print("\n4. Using interpolate method\n")
new_df = df.interpolate()
print(new_df)

    # lets use method in argument of interpolate
print("\ninterpolate with method argument\n")
new_df = df.interpolate(method="time")
print(new_df)

# 5. drop rows which have any na values.
# Note: index value is not being count in this method.
print("\n5. drop rows which have any na values...\n")
new_df = df.dropna()
print(new_df)

    # drop rows which have all na values.
print("\n drop rows which have all na values...\n")
new_df = df.dropna(how="all") # 9 jan row dropped
print(new_df)

    # Don't drop rows which have atleast one non na values. Use thresh=1 (threshold) in paremeter
print("\n Don't drop rows which have atleast one non na values...\n")
new_df = df.dropna(thresh=1) # 9 jan row dropped
print(new_df)

    # Don't drop rows which have atleast two non na values. Use thresh=2 (threshold) in paremeter
print("\n Don't drop rows which have atleast two non na values...\n")
new_df = df.dropna(thresh=2) # 6 and 9 jan row dropped
print(new_df)

# 6. reindex => to create new rows which are missing on the basis of index values
print("\n6. reindex => to create new rows which are missing on the basis of index values\n")
print("Current dataframe: \n", df)
dt = pd.date_range("01-01-2017", "01-11-2017") #mm-dd-yyyy
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
print("\n df after inserting date index: \n",df) # 2 and 3 jan are added