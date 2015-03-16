import psycopg2

def init_db():
  conn = psycopg2.connect('postgresql://{user}:{pwd}@localhost:5432/{database}'.format(user = 'Gregory', pwd='', database='template1'))
  cur = conn.cursor()
  return cur

def run_sql(cur, query):
  cur.execute(query)
  return cur.fetchall()
