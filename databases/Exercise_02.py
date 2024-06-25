'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

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
rental =  sqlalchemy.Table('rental', metadata, autoload_with=engine)
inventory = sqlalchemy.Table('inventory', metadata, autoload_with=engine)

#query = sqlalchemy.select(actor).where(actor.columns.first_name.in_(["JOHN", "JANE"])) 
#query = sqlalchemy.select(actor.columns.first_name, actor.columns.last_name, film.columns.title).where(sqlalchemy.and_(actor.columns.actor_id == film_actor.columns.actor_id, film_actor.columns.film_id == film.columns.film_id, actor.columns.first_name == "JOHN"))
#query = sqlalchemy.select(actor.columns.first_name.distinct(), actor.columns.last_name, category.columns.name).group_by(actor.columns.last_name, category.columns.name).where(sqlalchemy.and_(actor.columns.actor_id == film_actor.columns.actor_id, film_actor.columns.film_id == film_category.columns.film_id, film_category.columns.category_id == category.columns.category_id, actor.columns.first_name == "BOB", category.columns.name == "Comedy"))
query = sqlalchemy.select(film.columns.title, category.columns.name, rental.columns.rental_date).order_by(sqlalchemy.asc(rental.columns.rental_date)).where(sqlalchemy.and_(film.columns.film_id == inventory.columns.film_id, inventory.columns.inventory_id == rental.columns.inventory_id, film_category.columns.film_id == film.columns.film_id, film_category.columns.category_id == category.columns.category_id, category.columns.name == "Comedy"))

result_proxy = connection.execute(query)  
  
result_set = result_proxy.fetchall()  
print(result_set)