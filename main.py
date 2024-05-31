# import pandas as pd
import streamlit as st
import time

from Classes.StatusInvest import statusInv


def main():
    
    statusInv.setaAcoes(['bbas3', 'bbse3', 'fesa4', 'cmig4', 'neoe3', 'klbn11', 'taee11', 'itsa4','vale3','cxse3'])
    indicadores = statusInv.GetIndicadores()
    # st.write(indicadores)
    graham_method = statusInv.getGrahamMethod(indicadores)
  
 

    st.title("Graham method")
    st.dataframe(graham_method, hide_index=True)
    # st.table(graham_method)
    
    
    # stausInv.getValues()
    
 

if __name__ == "__main__":
    while True:
        main()
        time.sleep(5*60)
        st.rerun()
    # main()