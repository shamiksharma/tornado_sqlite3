import database

#
# can either specify a db file or use in-memory if no params provided
#conn = database_sqlite3.ConnectionSqlite3("test.db")
#

conn = database.Connection(":memory:")  

#
# create a table and insert sample data
#
conn.execute('create table users (id integer, name char(10));')
conn.execute('insert into  users (id, name) values (1, "jack");')
conn.execute('insert into  users (id, name) values (2, "jill");')

#
# retrieve each row as a dictionary
#
for user in conn.query("select * from users"):
  print "User %s has id %d" % (user.name, user.id)

#
# Get a specific user
#
user = conn.get("select * from users where id='2'")
if user:
 print "User 2 is : %s" % (user.name)
else:
 print "no users"
