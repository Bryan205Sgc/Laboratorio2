import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://bryan2:bryan123@LocalHost/GestorInventario?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)