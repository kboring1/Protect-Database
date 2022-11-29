from sqlalchemy import create_engine, Table, Column, Integer,String, MetaData
engine = create_engine('sqlite:///customerdata.db', echo = True)

meta = MetaData()
customers = Table(
    'customers personal data', meta,
    Column('id', Integer, primary_key = True),
    Column('address', String,),
    Column('Phone Number', Integer),
    Column('Card Number', Integer) 
)

conn = engine.connect()
conn.execute(customers.insert(),[
    {'address': '125 e leaf rd', 'Phone Number' : '', 'Card Number' :''},
    {'address': '', 'Phone Number' : '', 'Card Number' :''},
    {'address': '', 'Phone Number' : '', 'Card Number' :''},
    {'address': '', 'Phone Number' : '', 'Card Number' :''},
    {'address': '', 'Phone Number' : '', 'Card Number' :''}
])

meta.create_all(engine)