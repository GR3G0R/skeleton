import web
from dbindex import init_db, run_sql
from todo import Todo

urls = (
 '/hello', 'Index'
)

app = web.application(urls, globals())
db_cursor = init_db()

render = web.template.render('templates/')

class Index(object):
  def GET(self):
    # data = run_sql(db_cursor, 'select * from todo')
    first = Todo(db_cursor, 1)
    return render.hello_form(first)

  def POST(self):
    form = web.input(name="Nobady",greet="Hello")
    greeting = "%s, %s" % (form.greet, form.name)
    return render.index(greeting = greeting)



if __name__ == "__main__":
  app.run()

