import mysql.connector
import pandas as pd
empdata = pd.read_csv('Autogidas.csv', index_col=False, delimiter = ',')
empdata.head()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE Cars_Database")
#mydb.commit()

mycursor.execute("CREATE TABLE cars_data(Car_Model varchar(255),Price varchar(255),Parameters varchar(255),Link varchar(255))")
for i,row in empdata.iterrows():
  sql = "INSERT INTO Cars_Database.cars_data VALUES (%s,%s,%s,%s)"
  mycursor.execute(sql, tuple(row))
  mydb.commit()