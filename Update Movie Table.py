
# coding: utf-8

# In[ ]:

import pymysql as pys


# In[ ]:

db = pys.connect("localhost", "root", "password")
#Use password for your root@localhost
cur = db.cursor()
db.autocommit(True)


# In[ ]:

cur.execute("USE CS411")


# In[ ]:

cur.execute("Delete From CS411.Movie")


# In[ ]:

cur.execute("ALTER TABLE CS411.Movie ADD tconst VARCHAR(250)")
cur.execute("ALTER TABLE CS411.Movie ADD Genre VARCHAR(250)")
#Run the to_sql line from other python file


# In[ ]:

cur.execute("Select * From CS411.Movie")
cur.fetchall()

