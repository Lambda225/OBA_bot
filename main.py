import mysql.connector as connector
from fastapi import FastAPI
from pydantic import BaseModel

mydb = connector.connect(host='localhost',user='root',password='',database='bank')

app = FastAPI()

class Item(BaseModel):
    id_client: int




# mycursor.execute("SELECT * FROM bank_customer LIMIT 100")

@app.get('/')
def root(item:Item):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT b.balance  FROM bank_customer b WHERE b.customer_id = {item.id_client}")
    for i in mycursor:
        sold = i
    return {'sold':sold[0]}
