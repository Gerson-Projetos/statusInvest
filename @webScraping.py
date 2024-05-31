import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import math
import time



def main():
    st.title("Web Scraping with BeautifulSoup and Streamlit")

    URLs = {
                'bbse3': "https://statusinvest.com.br/acoes/bbse3",
                'taee11': "https://statusinvest.com.br/acoes/taee11",
                'cxse3': "https://statusinvest.com.br/acoes/cxse3",
                'klbn11': "https://statusinvest.com.br/acoes/klbn11",
                'bbas3': "https://statusinvest.com.br/acoes/bbas3",
            }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    dados = []
    titles = ['P/L','P/VP','VPA', 'LPA']
    valor_atual = []
    for _url in URLs:
        
        url = URLs[_url]
        
        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()  # Check if the request was successful
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the URL: {e}")
            return

        soup = BeautifulSoup(r.content, 'html5lib')  # Parse the HTML content
        pretty_html = soup.prettify()

        quotes=[]  # a list to store quotes 

        valor_atual.append({_url:soup.find('div', attrs ={'class': 'd-md-inline-block'}).find('strong', class_='value').text.strip()})
        
        table = soup.find('div', attrs ={'data-group': '0', 'class': 'indicators w-100'})
        
        
        for row in  table.findAll('div', 
                            attrs = {'class': 'item'}): 
            
            title_tag = row.find('h3', class_='title')
            value_tag = row.find('strong', class_='value')
            quote = {} 
            if title_tag and value_tag:
                if title_tag.text.strip() in titles:
                    quote['indicator'] = title_tag.text.strip()
                    quote['value']  = value_tag.text.strip()
                    quotes.append(quote) 

        dados.append({_url: quotes})
        
        
    # df = pd.DataFrame()
    values = {'Ação':[], 'Cotação':[], 'LPA':[], 'VPA':[], 'P/L':[], 'P/VP':[], 'Coeficiente':[], 'Valor justo':[], 'Margem de segurança':[]}



    # st.write(valor_atual[0]['bbse3'])
    
    
    for v1 in dados:
       for acao in v1:
            # values['Ação'].append(acao)
            values['Ação'].append(acao)
            
            for dict_ in valor_atual:
                # st.write(key)
                try:
                    values['Cotação'].append(dict_[acao])
                except:
                    pass
                 
            # st.write(acao)
            for dict_ in v1[acao]:
                values[dict_['indicator']].append(dict_['value'])
                

            # values['LPA'].append(v1[acao][''])
    
    
    
    for key in range(0, (len(values['Ação'])), 1):
        pl = values['P/L'][key].replace(',', '.')
        vp = values['P/VP'][key].replace(',', '.')
        vpa = values['VPA'][key].replace(',', '.')
        lpa = values['LPA'][key].replace(',', '.')
        cotacao = values['Cotação'][key].replace(',', '.')
        
        coef = float(pl) * float(vp)
        valor_justo = math.sqrt(float(vpa)*float(lpa)*coef)
        margen = (valor_justo*100)/(float(cotacao)-100)
        
        values['Coeficiente'].append(coef)
        values['Valor justo'].append(valor_justo)
        values['Margem de segurança'].append(margen)    
        
        
    df = pd.DataFrame(values)
    # dataPd = pd.DataFrame(dados
    # Display the HTML content in the Streamlit app
    st.subheader("Parsed HTML Content")
    # st.code(pretty_html, language='html')
    st.dataframe(df)
    

    
if __name__ == "__main__":
    
    while True:
        main()
        time.sleep(300)
        st.rerun()