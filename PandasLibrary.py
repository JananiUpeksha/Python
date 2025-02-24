import pandas as pd

data = {'Name': ['Alice','Bob','Charlie','David'],
        'Age': [25,30,35,40]}
df = pd.DataFrame(data)
print(df)
print(df.loc[1,"Name"])
print(df.loc[1,"Age"])
print(df.iloc[1,0])
print(df.iloc[0])
print(df.iloc[[0,1]])
print('-----------------------------------------------------------')

data = {
    "calaries": [450,380,390],
    "duration": [50,45,55]
}
df = pd.DataFrame(data,index = ["day1","day2","day3"])
print(df)
print(df['calaries'])
print('-----------------------------------------------------------')
print(df.loc["day2"])
print('-----------------------------------------------------------')
print(df.loc[["day1","day2"]])
print('-----------------------------------------------------------')
print(df.shape)
print(df.size)#row*columns
print('-----------------------------------------------------------')
print(df.columns)
print(list(df.columns))

#convert data frame into numpy array
print('-----------------------------------------------------------')
df = pd.DataFrame({'A':[1,2],'B':[3,4]})
print(df.values)
print(type(df.values))

#Functions
print('-----------------------------------------------------------')
print(len(df))  # Returns the number of rows in the DataFrame


#Statictics functions
print('-----------------------------------------------------------')
data = {
    "calaries": [450,380,390],
    "duration": [50,45,55]
}
df = pd.DataFrame(data)
print(df.mean())
print(df.sum())
print(df.describe())


"""
You are a data analysst for a retail company the company has provided you with data containing sales data 
your task is to anlyse the sales data  using python and pandas to answer some key business questions 
- calculte the total for each role - add a new col total revenew to store the total revenew for each order
- Identify the best selling product 
- find the product with the highest total sales revenew 
"""

data = {
    "Product": ['Laptop','Smart Phone','Desk Chair','Moniter','Book Shelf'],
    "Category": ['Electronic','Electronic','Furniture','Electronic','Furniture'],
    "Quantity": [2,5,10,4,2],
    "Price per Unit": [1000,800,150,200,300],
    "Region": ['North','South','East','West','North'],

}
print('-----------------------------------------------------------')
df = pd.DataFrame(data,index = [101,102,103,104,105])
print(df)

quantities = df['Quantity']
prices = df['Price per Unit']
total =  df['Quantity']*df['Price per Unit']
print(total)
df['Total'] = list(total)
print(df)

print('-----------------------------------------------------------')
filtered_df = df[df['Quantity']  > 5 ]
print(filtered_df,type(filtered_df))
#max = df['Quantity'].max()
#revenew = df['Total'].max()
revenew = df[df['Total']== df['Total'].max()]
print(revenew)
print('-----------------------------------------------------------')

#Adding a new row 
"""
df = pd.DataFrame({'A':[1,2],'B':[3,4]})
df.loc[len(df)] = [5,6]
"""

new_row = {
    "Product": "Table Lamp",
    "Category": "Furniture",
    "Quantity": 3,
    "Price per Unit": 120,
    "Region": "West",
    "Total": 3 * 120 
}
df.loc[len(df) + 101] = new_row  # Add new row with an appropriate index
print(df)
print('-----------------------------------------------------------')


#Remove - if axis = 1 -> remove col, if axis = 0 -> remove row
#drop colunm(lable,axis,inplace=false) false nm dnata thiyna df ekata mkuth wen na aluthma ekak return wenwa
df_dropped = df.drop('Region',axis=1)
print(df_dropped)
print('-----------------------------------------------------------')
# Drop row 
df_dropped = df.drop(103, axis=0)
print(df_dropped)
print('-----------------------------------------------------------')

#Import csv file as a dataframe
df = pd.read_csv('customers-10.csv')
print(df)
print('-----------------------------------------------------------')

"""
#Import json file as a dataframe
df = pd.read_json('example_1.json')
df = pd.DataFrame([data])  # Wrapping the dictionary in a list
print(df)
"""


