import mysql.connector

mydb = mysql.connector.connect (
	
	host = "mysql1",
	user="root",
	password="password",
	auth_plugin="mysql_native_password"

)

testcursor = mydb.cursor()
testcursor.execute("CREAT DATABASE studentdb")

testcursor.execute("SHOW DATABASE")

for x in testcursor:
	print(x)
