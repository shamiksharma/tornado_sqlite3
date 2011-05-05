
database.py is a thin wrapper over sqlite3. It allows python scripts to
retrieve and treat table records as dictionary objects. Thus a user row
with fields id and name, can be accessed thus

conn = database.Connection()
user = conn.get("select * from user where id=2")
print user.id + ":" +  user.name

It is derived from Tornado's MySQL adapter 
https://github.com/facebook/tornado/blob/master/tornado/database.py

It allows you to build Tornado apps that work with SQLite3
using the same API that Tornado provides in its database module.

This can be useful because Sqlite comes pre-installed with python
so it allows you to build a Test Tornado app without 
having to install MySQL.

database.py does not depend on Tornado, and can be used independent 
of Tornado, as illustrated in demo.py

To use database.py with Tornado, you can either replace tornado/database.py
with this database.py, or place database.py in your Python path,
and import database instead of import tornado.database


A sample program using database_sqlite3 is in demo.py
To run it  
% python demo.py

A sample Tornado app using database_sqlite3 is in demo_tornado.py
To run it  
% python tornado_demo.py
and open browser and go to 
http://localhost:8080/
http://localhost:8080/user/new?id=3&name=marcos
http://localhost:8080/user?id=3

