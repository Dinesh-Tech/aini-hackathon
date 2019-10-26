import numpy as np
import re

import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/bucket-8732/DatathonPeltarionChallenge/SF_Datathon_Data_Peltarion_compatible.csv')
df.to_csv("Datathon.csv")
df= pd.read_csv('Datathon.csv')

#print("Column headings:")
#print(df.columns)
#print(df['Gender'])

# print(df.index)
# for i in df.index:
#     if(df['id'][i].isnumeric()):
#         print("Yes")
#     else:
#         df['id'][i].replace(df['id'][i],value=i)
# print(df)


for i in df.index:
    valueOfI=df['id'][i]
    if re.match("^[0-9]*$", valueOfI):
        print("Valid")
    else:
        df["id"][i] = df["id"][i].replace(valueOfI, "Invalid")
        df["id"] = df["id"].replace("Invalid", i+1)

df.to_csv('CleanId.csv')



        #print(df["id"] )
# #df.to_csv('now3.csv') must

# df.sort_values(df['GPA'])
# print(df)
#df.to_csv('now4.csv')






#if (re.match("^[0-9]*$"), df['id'][49]):

#print(df['id'][100])


# df.sort_values(columns="Age")
# print(df)

# d= open('sheet.csv', 'r')
# ll=d.read().splitlines()
# print(ll[1])
# print(ll[2])
#
# ll.sort(columns="Age")
#
# print(ll[1])
# print(ll[2])

#
# filter = df["Name"]=="MISSING"
# if filter.any():
#     df["Name"]= df["Name"].replace("MISSING", np.NAN)
#



filter = df["Gender"] == "MISSING"
if filter.any():
    df["Gender"] = df["Gender"].replace("MISSING", np.NAN)



# filter = df["Race"] == "MISSING"
# if filter.any():
#     df["Race"] = df["Race"].replace("MISSING", np.NAN)
#
# df.ind

# df.to_csv("blankvalue.csv")
#




(df['Gender'].isnull())







#  df.to_csv('Gendertrueprint.csv')
#
#
# #print(df)














