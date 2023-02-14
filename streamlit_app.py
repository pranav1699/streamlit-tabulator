import streamlit as st
import pandas as pd
from tabulator_table import tabulator




st.set_page_config(layout="wide")
col1,col2,col3,col4 = st.tabs(['test','test1','test3','test4'])

with col1:
        df = pd.read_csv('test.csv')
        #df = df[0:100]
        con_df= df.to_json(orient='records')
        st.write(df)
        st.subheader("test table")
        st.button("Click me ..!")
        table_code_1 = """
            var table = new Tabulator("#example-table", {
            data: tabledata,
            renderHorizontal:"virtual",
            height: "350px",
            movableRows: true,
            groupBy:"Group",
            groupStartOpen:false,
            //movableRows: true,
            movableColumns: true,
            autoColumns: true
        });
            """
        tabulator(con_df,table_code_1,"test")
with col2 :
    df2 = pd.read_csv('test.csv')
    con_df2= df2.to_json(orient='records')
    st.write(df2)
    table_code_2 = """
            var table = new Tabulator("#example-table", {
            data: tabledata,
            renderHorizontal:"virtual",
            height: "350px",
            movableRows: true,
            groupBy:"Group",
            groupStartOpen:false,
            //movableRows: true,
            movableColumns: true,
            autoColumns: true
        }); """
    tabulator(con_df2,table_code_2,"test2")


with col3 :
    df2 = pd.read_csv('test.csv')
    con_df2= df2.to_json(orient='records')
    st.write(df2)
    table_code_3 = """
            var table = new Tabulator("#example-table", {
            data: tabledata,
            renderHorizontal:"virtual",
            height: "350px",
            movableRows: true,
            groupBy:"Group",
            groupStartOpen:false,
            //movableRows: true,
            movableColumns: true,
            autoColumns: true
        }); """
    tabulator(con_df2,table_code_3,"test3")

with col4 :
    df2 = pd.read_csv('test.csv')
    con_df2= df2.to_json(orient='records')
    st.write(df2)
    table_code = """
    var table = new Tabulator("#example-table", {
    data: tabledata,
    layout:"fitDataTable",
    height: "350px",
    movableRows: true,
    // groupBy:"Group",
    // groupStartOpen:false,
    //movableRows: true,
    movableColumns: true,
    autoColumns: true
  });
    """
    tabulator(con_df2,table_code,"test4")