import sqlite3
con = sqlite3.connect("survey.db")
cur = con.cursor()
cur.execute("SELECT * from Person;")
results = cur.fetchall()
#results = cur.fetch() just gets one of the results

#results are stored in an array (sequence and we go through them and print
for i in results
	print(i)


#MAke sure to close these	
cur.close()
con.close()