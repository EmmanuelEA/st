import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://usuario_consulta:platzicohort10@platzicohort10.cig2rbjhhqmz.us-east-1.rds.amazonaws.com/Brazilian_e_commerce')

with engine.connect() as con:
  rs = con.execute("SELECT product_id,price FROM olist_order_items_dataset WHERE price > 6000") # query que vamos a realizar
  df = pd.DataFrame(rs.fetchall()) # lectura de las filas, hay mas opciones
  df.columns = rs.keys()
  df = df.astype(str)

st.title('Datos de AWS, tabla olist_order_items_dataset')
st.text('consulta product_id con los precios mayores a 6000')
st.dataframe(data=df)
st.bar_chart(data=df)