
# coding: utf-8

# In[1]:

import pandas as pd
import csv
from ast import literal_eval
import numpy as np
import sqlalchemy


# In[2]:

basics_table = pd.read_csv('/Users/SrijanKhare/Documents/411 IMBd Datasets/title.basics.tsv', sep = '\t', 
                    dtype = {'startYear': object, 'endYear': object},
                                                converters = {'genre': literal_eval})
#Replace FilePath with your local filepath for all tables

ratings_table = pd.read_csv('/Users/SrijanKhare/Documents/411 IMBd Datasets/title.ratings.tsv', sep = '\t') 
crew_table =  pd.read_csv('/Users/SrijanKhare/Documents/411 IMBd Datasets/title.crew.tsv', sep = '\t')
name_table = pd.read_csv('/Users/SrijanKhare/Documents/411 IMBd Datasets/name.basics.tsv', sep = '\t')


# In[3]:

crew_table = crew_table[crew_table.directors != '\\N']
#Gets Rid of Movies with no directors
crew_table['directors'] = crew_table.directors.str.split(',').apply(lambda x: x[0])
#Picks the first director listed for each movie


# In[4]:

crew_table_with_name = pd.merge(crew_table, name_table[['nconst','primaryName']], left_on = 'directors', right_on = 'nconst', how = 'left')
crew_table_with_name = crew_table_with_name.drop(['writers', 'nconst'], axis = 1)


# In[5]:

temp = pd.merge(basics_table, crew_table_with_name[['tconst','primaryName']], on = 'tconst')
movie_table = pd.merge(temp, ratings_table, on = 'tconst')
movie_table.columns = ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult',
       'startYear', 'endYear', 'runtimeMinutes', 'genres', 'directorName',
       'averageRating', 'numVotes']
movie_table = movie_table.loc[movie_table['titleType'] == 'movie']
movie_table = movie_table.drop(['originalTitle', 'isAdult'
    ], axis = 1)


# In[7]:

movie_sql_table = movie_table[['tconst','primaryTitle', 'startYear', 'directorName', 'averageRating', 'genres']]
movie_table = movie_table[movie_table.genres != '\\N']
movie_table['genres'] = movie_table.genres.str.split(',').apply(lambda x: x[0])
movie_sql_table.columns = ['tconst','Title', 'Year', 'Director', 'Rating', 'Genre']
movie_sql_table = movie_sql_table.loc[movie_sql_table['Year'] != '\\N']


# In[ ]:

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/CS411')
#replace password with your own localhost password
con = engine.connect()
movie_sql_table.to_sql(name = 'Movie', con = con, if_exists= 'append', index = False)

