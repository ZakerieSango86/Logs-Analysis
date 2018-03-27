import psycopg2
import bleach

def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect("dbname=forum")
    c = db.cursor()
    query = "select content, time from posts order by time desc"
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect("dbname=forum")
  c = db.cursor()
#  insert = "insert into posts values(%s)",(content,)
  c.execute("insert into posts values(%s)",(bleach.clean(content),))
  db.commit()
  db.close()


# "Database code" for the DB Forum.

#import datetime

#POSTS = [("This is the first post.", datetime.datetime.now())]

#def get_posts():
#  """Return all posts from the 'database', most recent first."""
#  return reversed(POSTS)

#def add_post(content):
#  """Add a post to the 'database' with the current timestamp."""
#  POSTS.append((content, datetime.datetime.now()))
#"""
