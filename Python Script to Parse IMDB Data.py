
# coding: utf-8

# In[124]:

import pandas as pd
import csv
from ast import literal_eval
import numpy as np
import sqlalchemy


# In[ ]:

basics_table = pd.read_csv('/Users/SrijanKhare/Documents/411 IMBd Datasets/title.basics.tsv', sep = '\t', 
                    dtype = {'startYear': object, 'endYear': object},
                                                converters = {'genre': literal_eval})
#Replace FilePath with your local filepath for all tables


# In[ ]:

ratings_table = pd.read_csv('/Users/SrijanKhare/Documents/411 IMBd Datasets/title.ratings.tsv', sep = '\t') 


# In[ ]:

crew_table =  pd.read_csv('/Users/SrijanKhare/Documents/411 IMBd Datasets/title.crew.tsv', sep = '\t')


# In[ ]:

name_table = pd.read_csv('/Users/SrijanKhare/Documents/411 IMBd Datasets/name.basics.tsv', sep = '\t')


# In[ ]:

crew_table = crew_table[crew_table.directors != '\\N']
#Gets Rid of Movies with no directors
crew_table['directors'] = crew_table.directors.str.split(',').apply(lambda x: x[0])
#Picks the first director listed for each movie


# In[ ]:

crew_table_with_name = pd.merge(crew_table, name_table[['nconst','primaryName']], left_on = 'directors', right_on = 'nconst', how = 'left')


# In[ ]:

crew_table_with_name = crew_table_with_name.drop(['writers', 'nconst'], axis = 1)


# In[ ]:

temp = pd.merge(basics_table, crew_table_with_name[['tconst','primaryName']], on = 'tconst')
movie_table = pd.merge(temp, ratings_table, on = 'tconst')


# In[ ]:

movie_table.columns = ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult',
       'startYear', 'endYear', 'runtimeMinutes', 'genres', 'directorName',
       'averageRating', 'numVotes']


# In[ ]:

movie_table = movie_table.loc[movie_table['titleType'] == 'movie']


# In[ ]:

movie_table = movie_table.drop(['originalTitle', 'isAdult'
    ], axis = 1)


# In[ ]:

movie_genre_table = movie_table[['tconst', 'primaryTitle', 'genres']]


# In[144]:

movie_sql_table = movie_table[['primaryTitle', 'startYear', 'directorName', 'averageRating']]
movie_sql_table.columns = ['Title', 'Year', 'Director', 'Rating']


# In[145]:

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/CS411')
#replace password with your own localhost password


# In[146]:

con = engine.connect()


# In[158]:

movie_sql_table = movie_sql_table.loc[movie_sql_table['Year'] != '\\N']


# In[160]:

movie_sql_table.to_sql(name = 'Movie', con = con, if_exists= 'append', index = False)


# In[ ]:



