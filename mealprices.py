from sqlalchemy import create_engine, Table, Column, Integer,String, MetaData
engine = create_engine('sqlite:///customerdata.db', echo = True)

meta = MetaData()
customers = Table(
    'customers', meta,
    Column('id', Integer, primary_key = True),
    Column('Meals', float),
    Column('Prices', float) 
)

conn = engine.connect()
conn.execute(customers.insert(),[
    {'Meals': '', 'Prices' : ''},
    {'Meals': '', 'Prices' : ''},
    {'Meals': '', 'Prices' : ''},
    {'Meals': '', 'Prices' : ''},
    {'Meals': '', 'Prices' : ''},
])
