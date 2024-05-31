# import pandas as pd
import streamlit as st
# import time

from Classes.StatusInvest import statusInv

def main():
    
    statusInv.setaAcoes(['bbas3', 'bbse3'])
    indicadores = statusInv.GetIndicadores()
    graham_method = statusInv.getGrahamMethod(indicadores)
   
    st.write(graham_method)
    
    
    # stausInv.getValues()
    
 

if __name__ == "__main__":
    #  while True:
    #     main()
    #     time.sleep(5*60)
    #     st.rerun()
    main()