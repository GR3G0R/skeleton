from dbindex import init_db, run_sql

class Todo(object):
  def __init__(self, db_cursor, id):
    data = run_sql(db_cursor, 'select * from todo where id = {id}'.format(id=id))[0]
    self.id = int(data[0])
    self.text = data[1]
    self.created_at = str(data[2])
    self.done = data[3]

  # def setText(text):
  #   # db command to write text to db
  #
  # def setDone(boolean):
  #   # db command to write boolean to db
