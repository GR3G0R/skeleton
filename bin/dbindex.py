import psycopg2

def init_db():
  conn = psycopg2.connect('postgresql://{user}:{pwd}@localhost:5432/{database}'.format(
    user = 'gregory', pwd='yourpwd', database='todo'))
  cur = conn.cur()
  return cur

def run_sql(cur, query):
  response = cur.execute(query)
  return response.fetchAll()
