import json as jsn
import requests as req
import streamlit as st



class ConfigReq():
    
    _header = {}
    _urls = {}

    def __init__(self) -> None:
        pass


    def setHeader(self, header=False):
        if header:
            
            self._header = header
        else:
            self._header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
            }
        
        
    def setUrl(self, urls=False):
        self._urls = urls
        

    
