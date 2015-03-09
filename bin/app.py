import web

urls = (
 '/', 'index'
)

app = web.application(urls,globals())

class index(object):
  def GET(self):
    greeting = "Hello World"
    return render.index(greeting = greeting)
    
render = web.template.render('templates/')


if __name__ == "__main__":
  app.run()

