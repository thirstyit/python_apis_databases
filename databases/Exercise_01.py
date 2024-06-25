'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy
import keys



engine = sqlalchemy.create_engine('mysql+pymysql://'+ keys.root +':' + keys.pwd + '@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload_with=engine) 
category = sqlalchemy.Table('category', metadata, autoload_with=engine) 

print(repr(metadata.tables['film']))
print(repr(metadata.tables['category']))