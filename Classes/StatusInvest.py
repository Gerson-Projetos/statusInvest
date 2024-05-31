import requests as req
import streamlit as st
from bs4 import BeautifulSoup

from Classes.ConfigRequisicao import ConfigReq


class StatusInvest(ConfigReq):

    _acoes = ''
    
    def __init__(self) -> None:
        super().__init__()
        
        self.setHeader()
        self.setUrl({
            'indicadores': 'https://statusinvest.com.br/acao/indicatorhistoricallist',
            'valoresAtuais': 'https://statusinvest.com.br/acoes/'
        })
        
        # pass
   
    def setaAcoes(self, acoes=''):
        self._acoes = acoes
        
        
    
    def GetIndicadores(self):
        
        url = self._urls['indicadores']
        valores_atuais = self.getValues()
        # st.write(valores_atuais)
        
        data = {}
        for acao in self._acoes:
            data[acao] = {
                    'codes[]': acao,
                    'time': '5',
                    'byQuarter': 'false',
                    'futureData': 'false'
            }
        
        # st.write(data)
        # for name in self.acoes:
        # params = {'codes': ['bbas3'], 'time': 5, 'byQuarter': False, 'futureData': False}
        
        resp = {}
        for acao in data:
            # st.write(acao)
            resp[acao] = req.post(url, data=data[acao], headers=self._header)

        # st.write(resp)
       
        dadoFiltrado = {}
        for acao in resp:
            rs = resp[acao]
            
            if rs.status_code == 200:
                _dict_data = dict(rs.json())
                # st.write(_dict_data)
                dados = _dict_data['data']
                estatistica = {}
                
                indicadores = ['p_l', 'p_vp','lpa','vpa', 'dy', 'roe']
                # st.write(data['data'])
                try:
                    for acao in dados:
                        for _indicadores in dados[acao]:
                            # st.write(_indicadores['key'])
                            if _indicadores['key'] in indicadores:
                                estatistica['vl'] = valores_atuais[acao]
                                estatistica[_indicadores['key']] = _indicadores
                                
                                
                    dadoFiltrado[acao] = estatistica    
                except:
                    err = {'error': f"Error: Dados da ação *{acao.upper()}* não encotrados"}
                    dadoFiltrado[acao] = err
            else:
                # If not successful, display an error message
                err = {'error':f"Error: {rs.status_code} - {rs.reason}"}
                dadoFiltrado[acao] = err    
                # st.error()
                
        return dadoFiltrado
    
    def getValues(self):

        URLs = {}
        for acao in self._acoes:
            URLs[acao] = self._urls['valoresAtuais']+acao

        valor_atual = {}
        for acao in URLs:
            
            url = URLs[acao]
            
            try:
                r = req.get(url, headers=self._header)
                r.raise_for_status()  # Check if the request was successful
                
                soup = BeautifulSoup(r.content, 'html5lib')  # Parse the HTML content
                value = {acao:soup.find('div', attrs ={'class': 'd-md-inline-block'}).find('strong', class_='value').text.strip()}
                valor_atual[acao] = {"key": "vl", "actual": value[acao]}
            except req.exceptions.RequestException as e:
                erro ={'error': f"{e}"}
                valor_atual[acao] = erro

        return valor_atual
            
stausInv = StatusInvest()