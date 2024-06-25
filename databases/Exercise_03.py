'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''

import sqlalchemy
import keys
import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://'+ keys.root +':' + keys.pwd + '@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()  
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload_with=engine)  
category = sqlalchemy.Table('category', metadata, autoload_with=engine) 
film_category = sqlalchemy.Table('film_category', metadata, autoload_with=engine) 
film_actor = sqlalchemy.Table('film_actor', metadata, autoload_with=engine)
#rental =  sqlalchemy.Table('rental', metadata, autoload_with=engine)
#inventory = sqlalchemy.Table('inventory', metadata, autoload_with=engine)

query = sqlalchemy.update(film).values(rental_duration=5).where(film.columns.length >= 150)

#query = sqlalchemy.select(film.columns.rental_duration, film.columns.last_update).where(film.columns.length >= 150)

result_proxy = connection.execute(query)  
result_set = result_proxy.fetchall()  
print(result_set)