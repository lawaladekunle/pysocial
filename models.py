import sqlite3

ROOT = path.dirname(path.relpath((_file_))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'pysocialdatabase.db'))
    cur = con.cusor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, post))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'pysocialdatabase.db'))
    cur = con.cusor()
    cur.execute('select * from posts')
    post = cur.fetchall()
    return posts
