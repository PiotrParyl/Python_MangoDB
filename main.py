from http import client
from pydoc import cli
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("mango_pwd")

connection_str = f"mongodb+srv://maczo1928:{password}@test.subaa4r.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_str)

dbs = client.list_database_names()
print(dbs)