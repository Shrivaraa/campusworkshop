"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaabdik728r8866gg80-a.oregon-postgres.render.com",
        database="todoapp_sck3",
        user="root",
        password="vFhKBTf8XCdgft09efzXWatbZiM6BpL5")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
