from passlib.hash import sha512_crypt as sha
password = sha.hash("pass123")
print(password)
from database import db

mydb = db('root', '127.0.0.1', 'pass123', 'ARMS')
query = "update users set password = '{}' where username = 'QaisarAhmad'".format(password)

mydb.cursor.execute(query)
mydb.db.commit()