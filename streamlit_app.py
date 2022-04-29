import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
#import psycopg2
#from psycopg2 import DatabaseError

engine = create_engine('postgresql://usuario_consulta:platzicohort10@platzicohort10.cig2rbjhhqmz.us-east-1.rds.amazonaws.com/Brazilian_e_commerce')

with engine.connect() as con:
  rs = con.execute("SELECT product_id,price FROM olist_order_items_dataset WHERE price > 3000") # query que vamos a realizar
  df = pd.DataFrame(rs.fetchall()) # lectura de las filas, hay mas opciones
  df.columns = rs.keys()
#  df.columns = ['product_id','price']
 

st.dataframe(data=df)
st.bar_chart(data=df)