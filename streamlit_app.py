import streamlit as st
import pandas as pd
import psycopg2
from psycopg2 import DatabaseError

try:
    connection = psycopg2.connect(
        host='platzicohort10.cig2rbjhhqmz.us-east-1.rds.amazonaws.com',
        user='usuario_consulta',
        password='platzicohort10',
        database='Brazilian_e_commerce'
    )

    print("Conexión exitosa.")
    cursor = connection.cursor()
    #cursor.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'")
    cursor.execute("SELECT product_id,price FROM olist_order_items_dataset WHERE price > 3000")
    row = cursor.fetchall()
    #print(format(row))
    df = pd.DataFrame(row)
    df.columns = ['product_id','price']
    df = df.astype(str) 
    #print(df.head())
    #print(df.dtypes)
except DatabaseError as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")


st.dataframe(data=df)
st.bar_chart(data=df)