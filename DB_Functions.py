from peewee import MySQLDatabase, Model, TextField, BooleanField, DateField, PrimaryKeyField
from datetime import date
from Settings import *

connection = MySQLDatabase(DATABASE_NAME, # Connection to database
                         user=USER, password=PASSWORD) 

class ModelBase(Model):
    class Meta:
        database = connection
        
class products(ModelBase):
    ProdID = PrimaryKeyField()
    ProdName = TextField()
    ProdInStock = BooleanField()
    ProdDate = DateField()
    
def add_product(productNAME:str, productONSTOCK:bool, productDATE:date): # add product in table
    products.create(
                ProdName = productNAME,
                ProdInStock = productONSTOCK,
                ProdDate = productDATE
                )

def get_last_id(Table: str) -> int: # get last id from table
    cursor = connection.execute_sql(f'SELECT ProdID FROM {Table}')
    for id in cursor:
        pass
    return id+1

def get_products(Table: str): # get all entity's from table (should use for loop to unpack values)
    cursor = connection.execute_sql(f'SELECT * FROM {Table}')
    return cursor

def delete_product_byID(Table: str, ID: int) -> bool:
    products.delete().where(products.ProdID == ID).execute()  # delete product from table by ID
    query = products.update(ProdID=products.ProdID - 1).where(products.ProdID > ID) # balance id's after ID we deleted
    query.execute()
    return True

