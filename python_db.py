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

        cur.executescript("""DROP TABLE IF EXISTS Pets;
                         CREATE TABLE Pets(id INT, Name TEXT, Price INT);
                         INSERT INTO Pets VALUES(1, 'Cat', 4000);
                         INSERT INTO Pets VALUES(2, 'Rabbit', 1000);""")

        pets = ((3, 'Dog', 10000),
                (4, 'Monkey', 2000),
                (5, 'Bird', 1200))

        cur.executemany("INSERT INTO Pets VALUES(?,?,?)", pets)

        # will replace these statements with one.
        # cur.execute('SELECT SQLITE_VERSION()')
        # cur.execute("CREATE TABLE Pets(id INT, Name TEXT, Price INT)")
        # cur.execute("INSERT INTO Pets VALUES(1, 'Cat', 4000)")
        # cur.execute("INSERT INTO Pets VALUES(2, 'Rabbit', 1000)")
        # cur.execute("INSERT INTO Pets VALUES(3, 'Dog', 10000)")
        # cur.execute("INSERT INTO Pets VALUES(4, 'Monkey', 2000)")

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


# Multiple Queries
# The python database standard supports making multiple queries with one command.
# This can either be done through the executescript() method.
# which takes  a string of sql statements separated by a ';' semi-colon.

# Or we can use the parameterized sql statement executemany(template, data)
# This takes a string template of the query as the first argument
# and then a tuple of tuples of the data to use with the argument
# e.g. Executemany("INSERT INTO Pets VALUES(?, ?, ?)", data)
