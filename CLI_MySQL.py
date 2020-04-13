import mysql.connector
import difflib
#this one uses PHPMyAdmin and MySQL Database
con = mysql.connector.connect(
    user = username,
    password = pw,
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

cursor = con.cursor()
word = str(input("Enter the word : "))
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    #could do get_close_matches(word) like GUI.Py
    pass
