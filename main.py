

from h11 import Data
import pandas as pd
import bs4
import sqlalchemy
from DatabaseHandler import DatabaseHandler

class Main:
    db = None
    def __init__(self):
        db = DatabaseHandler()


Main()
