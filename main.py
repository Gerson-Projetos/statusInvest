# import pandas as pd
import streamlit as st
import time

from Classes.StatusInvest import stausInv

def main():
    
    stausInv.setaAcoes(['bbas3', 'bbse3'])
    indicadores = stausInv.GetIndicadores()
    
    st.write(indicadores)
    
    
    # stausInv.getValues()
    
 

if __name__ == "__main__":
    #  while True:
    #     main()
    #     time.sleep(5*60)
    #     st.rerun()
    main()