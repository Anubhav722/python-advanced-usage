# connect(info) - to connect to the database
# cursor() - will get a cursor object ready to execute queries.
# execute(sql) - an sql query
# fetchone() - returns just one row.
# fetchall() - returns a list of lists.
# commit() - saves the changes on the db.
# rollback() - rolls all temporary changes back.
# close() - closes the connection up.
# executemany() - executes a parameterized query.
# executescript() - executes a string of multiple SQL statements separated by a semi-colon

# We are using sqlite here.

import sqlite3

def Main():
	try:
		con = sqlite3.connect('test.db')
		cur = con.cursor()
		# cur.execute('SELECT SQLITE_VERSION()')
		cur.execute("CREATE TABLE Pets(id INT, Name TEXT, Price INT)")
		cur.execute("INSERT INTO Pets VALUES(1, 'Cat', 4000)")
		cur.execute("INSERT INTO Pets VALUES(2, 'Rabbit', 1000)")
		cur.execute("INSERT INTO Pets VALUES(3, 'Dog', 10000)")
		cur.execute("INSERT INTO Pets VALUES(4, 'Monkey', 2000)")

		con.commit()

		cur.execute("SELECT * FROM Pets")

		data = cur.fetchall()
		# data = cur.fetchone()
		# print(data)

		for row in data:
			print(row)

		con.close()

	except sqlite3.Error:
		if con:
			print("Error! rolling back")
			con.rollback()

	finally:
		if con:
			con.close()

if __name__ == '__main__':
	Main()
