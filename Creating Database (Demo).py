
# coding: utf-8

# In[ ]:

import pymysql as pys


# In[ ]:

db = pys.connect("localhost", "root", "password")
#USE password for localhost


# In[ ]:

cur = db.cursor()
db.autocommit(True)


# In[ ]:

cur.execute("show databases;")


# In[ ]:

cur.execute("CREATE Database CS411")


# In[ ]:

cur.execute("USE CS411")


# In[ ]:

create_movie_table = """Create Table CS411.Movie (
               Movie_ID INT NOT NULL AUTO_INCREMENT,
               Title VARCHAR(250) NOT NULL,
               Year INT,
               Director VARCHAR(250),
               Rating FLOAT,
               Primary Key(Movie_ID))"""
create_genre_table = """Create Table CS411.Genre (
                   Genre_ID INT NOT NULL AUTO_INCREMENT,
                   Genre_Name VARCHAR(250),
                   Primary Key(Genre_ID))"""
create_movie_genre_relationship = """Create Table CS411.Genre_Movie (
                   Genre_ID INT NOT NULL ,
                   Movie_ID INT NOT NULL,
                   Primary Key(Genre_ID, Movie_ID),
                   Foreign Key(Genre_ID) References CS411.Genre(Genre_ID),
                   Foreign Key(Movie_ID) References CS411.Movie(Movie_ID)
                   )"""
create_user_table = """Create Table CS411.User (
               User_ID INT NOT NULL AUTO_INCREMENT,
               Name VARCHAR(250) NOT NULL,
               Age INT,
               Gender VARCHAR(250),
               Primary Key(User_ID))"""
create_rating_table = """Create Table CS411.Rating (
               Comment_ID INT NOT NULL AUTO_INCREMENT,
               Comments VARCHAR(1000),
               Score INT,
               Primary Key(Comment_ID))"""
create_rate_movie_table = """Create Table CS411.Rate_Movie (
                   User_ID INT NOT NULL ,
                   Movie_ID INT NOT NULL,
                   Comment_ID INT NOT NULL,
                   Primary Key(Comment_ID),
                   Foreign Key(User_ID) References CS411.User(User_ID),
                   Foreign Key(Movie_ID) References CS411.Movie(Movie_ID),
                   Foreign Key(Comment_ID) References CS411.Rating(Comment_ID)
                   )"""


# In[ ]:

cur.execute(create_movie_table)


# In[ ]:

cur.execute(create_genre_table)


# In[ ]:

cur.execute(create_movie_genre_relationship)


# In[ ]:

cur.execute(create_user_table)


# In[ ]:

cur.execute(create_rating_table)


# In[ ]:

cur.execute(create_rate_movie_table)


# In[ ]:

cur.execute("show tables;")
cur.fetchall()


# In[ ]:
db.close()
