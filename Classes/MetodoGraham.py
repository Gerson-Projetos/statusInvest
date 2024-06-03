import pandas as pd
import math



class Graham():
    def __init__(self) -> None:
        pass
    
        
    def getIndicadores(self, dados):
        graham_data = {  
            'Ticker': [],
            'Cotação':[],
            'LPA': [],
            'VPA': [],
            'P/L Hist': [],
            'P/VP Hist': [],
            'DY': [],
            'Coeficiente': [],
            'Valor justo': [],
            'Margem de Seg(%)': []
        }
        for acao in dados:
            plH = dados[acao]['p_l']['avg']
            vpH = dados[acao]['p_vp']['avg']
            vpa = dados[acao]['vpa']['actual']
            lpa = dados[acao]['lpa']['actual']
            dy = dados[acao]['dy']['actual']
            cotacao = dados[acao]['vl']['actual'].replace(',', '.')

            coef = float(plH) * float(vpH)
            valor_justo = math.sqrt(float(vpa)*float(lpa)*coef)
            margen = (valor_justo*100)/(float(cotacao))-100

            graham_data['Ticker'].append(acao.upper())
            graham_data['Cotação'].append(cotacao)

            graham_data['VPA'].append(vpa)
            graham_data['LPA'].append(lpa)


            graham_data['P/L Hist'].append(plH)
            graham_data['P/VP Hist'].append(vpH)

            graham_data['DY'].append(dy)
            
            graham_data['Coeficiente'].append(coef)
            graham_data['Valor justo'].append(valor_justo)
            graham_data['Margem de Seg(%)'].append(margen)    


        df = pd.DataFrame(graham_data)
        df_filtrado = self.formatPd(df)

        return df_filtrado
    
    
    def formatPd(self, df):
        df_copy = df.copy()
        
        df_copy = df_copy.style.map(self.color_mrg, subset=['Margem de Seg(%)']).format({'Margem de Seg(%)': self.format_as_percentage})
        # df_copy = df_copy.applymap(lambda x: self.color_valorJusto(x,15 ))
        # df_copy = df_copy.apply(self.color_valorJusto, axis=1)
        df_copy = df_copy.format(self.format)

        return df_copy 
    
    def color_mrg(self, value):

        if value < 5:
            color = 'red'
        elif value > 20:
            color = 'green'
        else:
            color = 'black'

        return 'color: %s' % color
    
    def color_valorJusto(self, valor):
        if valor['Valor justo'] > float(valor['Cotação']):
            # color = 'red'
            return ['color: green']*len(valor)
        elif valor['Valor justo'] < float(valor['Cotação']):
            return ['color: red']*len(valor)
            # color = 'green'
        else:
            return ['']*len(valor)
        #    color = 'black'

        return 'color: %s' % color

    def format_as_percentage(self, value):
        if isinstance(value, float):
            return "{:.2f}%".format(value)
        else:
            return value
        
    def format(self, value):

        if isinstance(value, float):
            return "{:.2f}".format(value)
        else:
            return value
        
        
metodoGraham = Graham()