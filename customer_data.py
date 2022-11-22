from sqlalchemy import create_engine, Table, Column, Integer,String, MetaData
engine = create_engine('sqlite:///customerdata.db', echo = True)

meta = MetaData()
customers = Table(
    'customers', meta,
    Column('id', Integer, primary_key = True),
    Column('firstname', String),
    Column('lastname', String) 
)

conn = engine.connect()
conn.execute(customers.insert(),[
    {'firstname': 'James', 'lastname' : 'Morgan'},
    {'firstname': 'Kerry', 'lastname' : 'Madison'},
    {'firstname': 'John', 'lastname' : 'Jameson'},
    {'firstname': 'Sarah', 'lastname' : 'Willams'},
    {'firstname': 'Kalie', 'lastname' : 'Pearson'},
])

