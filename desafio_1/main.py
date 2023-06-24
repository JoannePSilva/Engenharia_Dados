import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv 
import os
import json

load_dotenv()

user = os.environ['POSTGRES_USER']
db = os.environ['POSTGRES_DB']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
con = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{db}').connect()

df = pd.read_csv('files/NBA Payroll(1990-2023).csv')
df.to_sql(name='nba_payroll', con=con, schema='desafio')

df = pd.read_csv('files/NBA Player Stats(1950 - 2022).csv')
df.to_sql(name='nba_player_stats', con=con, schema='desafio')

df = pd.read_csv('files/NBA Salaries(1990-2023).csv')
df.to_sql(name='nba_salaries', con=con, schema='desafio')

df = pd.read_csv('files/NBA Player Box Score Stats(1950 - 2022).csv')
df.to_sql(name='nba_Box_Score_Stats', con=con, schema='desafio')

with open ('files/json_data.json') as f:
    data = json.load(f)
    
df = pd.json_normalize(data)
df.to_sql(name='nba_TopTech_Startups', con=con, schema='desafio')
