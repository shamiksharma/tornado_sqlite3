import tornado.web
import tornado.httpserver
import tornado.ioloop
import database

class BaseHandler(tornado.web.RequestHandler):
  @property
  def db(self):
    return self.application.db

#
# Creates a new user, when you hit the url
# http://localhost:8080/user/new?id=100&name=jane
#

class NewUserHandler(BaseHandler):
  def get(self):
    idstr = self.get_argument("id", 10)
    id = int(idstr)
    name = self.get_argument("name", "john")
    sqlstr = 'insert into users (id,name) values (%d, "%s");' % (id,name) 
    self.db.execute(sqlstr)
    
#
# Get all users if you go to 
# http://localhost:8080/   or
# http://localhost:8080/user 
#
# Get a specific user (e.g. id=100) if you go to
# http://localhost:8080/user?id=2
#
#
class GetUserHandler(BaseHandler):
  def get(self):
    idstr = self.get_argument("id", "0")
    id = int(idstr)

    # if no id, get all users. Else get the specific id
    if id == 0:
      userList = self.db.query("select * from users") 
      if userList is None: userList = []
    else:
      sqlstr = 'select * from users where id = %d' % (id)
      user = self.db.get(sqlstr)
      userList = [user]

    outp = ""
    for user in userList:
      outp = outp + "<br> user (%d) => %s" % (user.id, user.name)
    self.write("<html><body>" + outp + "</body></html>")

class Application(tornado.web.Application):
  def __init__(self):
    handlers =  [ (r"/", GetUserHandler), (r"/user/new", NewUserHandler), (r"/user", GetUserHandler) ]
    settings = {}
    tornado.web.Application.__init__(self, handlers, **settings)

    self.db = database.Connection()
    self.db.execute('create table users (id integer, name char(20));')
    self.db.execute('insert into users (id, name) values (1,"jack");')
    self.db.execute('insert into users (id, name) values (2,"jill");')

def main():
    settings = { } 
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
