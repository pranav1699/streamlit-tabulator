import streamlit as st
import pandas as pd
from tabulator_table import tabulator

st.set_page_config(layout="wide")
df = pd.read_csv('test.csv')
#df = df[0:100]
con_df= df.to_json(orient='records')
st.write(df)
st.subheader("MT5 deals table")
tabulator(con_df)

# df2 = pd.read_csv('test.csv')
# con_df2= df2.to_json(orient='records')
# st.write(df2)
# tabulator(con_df2)

