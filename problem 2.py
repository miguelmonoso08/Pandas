import pandas as pd
cars = pd.read_csv ('cars.csv')
print('a') 
print(cars.iloc[0:5:,range(0,11,2)])

print('b')
print(cars.loc[cars['Model']=='Mazda RX4'])

print('c')
print(cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']])

print('d')
print(cars.loc[cars['Model']=='Mazda RX4',['Model','cyl','gear']])
print(cars.loc[cars['Model']=='Ford Pantera L',['Model','cyl','gear']])
print(cars.loc[cars['Model']=='Hona Civic',['Model','cyl','gear']])

