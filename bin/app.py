import web
from dbindex import init_db, run_sql

urls = (
 '/hello', 'Index'
)

app = web.application(urls, globals())
db_cursor = init_db()

render = web.template.render('templates/')h
class Index(objecth
  def GET(self):
    data = run_sql(db_cursor, 'select description, deadline from todoTasks')
    return render.hello_form()
   
  def POST(self):
    form = web.input(name="Nobady",greet="Hello")
    greeting = "%s, %s" % (form.greet, form.name)
    return render.index(greeting = greeting)
    


if __name__ == "__main__":
  app.run()

