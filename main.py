# -*- coding: utf-8 -*-

import re
import itertools



class Tweet:
    
    __autor        = ''
    __menciones    = []
    __etiquetas    = []
    __urls         = []
    __tipo         = []

    
    def __init__(self, autor, menciones, etiquetas, urls, tipo):
        self.__autor        = autor
        self.__menciones    = set(menciones)
        self.__etiquetas    = set(etiquetas)
        self.__urls         = set(urls)
        self.__tipo         = tipo

    def getAutor (self):
        return self.__autor
        
    def getAll (self):        
        return (self.__autor + '|')+ ':'.join (self.__etiquetas)  + '|' + ':'.join(self.__menciones)\
            + '|' + ':'.join(self.__urls ) + '|' + '|' + self.__tipo


    
def getData ( cad ):
    
    listatw = cad.split('|')      
    
    cad = listatw[0].strip()
    
    #########################################    
    #PRIMERO TRATAMOS LOS AUTORES Y MENCIONES
    #########################################
    
    #El autor es la primera arroba:    
    match = re.search (r'@[\w\.-]+', cad) 
    autor =  match.group(0)
    
    #Dejamos la cadena sin el autor para seguir buscando en ella:
    inicio_autor = cad.find('@') + 1
    fin_autor = cad.find(' ',inicio_autor)
    cad = cad[fin_autor+1:]
    
    #Buscamos todas las menciones que aparezcan:
    match_menciones = re.findall(r'@[\w\.-]+', cad)
    
    #y las etiquetas:
    match_etiquetas = re.findall(r'#[\w\.-]+', cad)
    
    #y las urls:
    match_urls = re.findall(r'(https?://[^\s]+)',cad)
    



    #########################################    
    #DESPUES TRATAMOS LOS TWEETS:
    #########################################
    cad = listatw[1].strip()
    
    #El inicio de la cadena nos da informacion del tipo:
    tipo = 'TW'

    #Vemos si tweet, rt o mencion:
    if (cad[0:2] == 'RT'):
        tipo = 'RT'

    if (cad[0:1] == '@'):
        tipo = 'RP'
    
        
    #import ipdb ; ipdb.set_trace ()

    #RTs
    #match_rts = re.findall(r'(RT ?[^\s]+)',cad)

    match_menciones = re.findall(r'@[\w\.-]+', cad)
    
    #y las etiquetas:
    match_etiquetas = re.findall(r'#[\w\.-]+', cad)
    
    #y las urls:
    match_urls = re.findall(r'(https?://[^\s]+)',cad)
    
    
    for  word in (match_menciones + match_etiquetas + match_urls):
        cad = cad.replace (word,'')
    
    print cad
    #import ipdb ; ipdb.set_trace()
    
    
    

    
    tw = Tweet (autor, match_menciones, match_etiquetas, match_urls, tipo)
    
    return tw


if __name__ == "__main__":
    
    f_autores = 'Data/autoresYmenciones_red.txt'
    f_tweets  = 'Data/tweets_red.txt'
    
    with open(f_autores) as f:
        autores_menciones = f.readlines()
        
    with open(f_tweets) as f:
        tweets = f.readlines()
        

    #Juntamos cada linea de cada lista en una nueva lista
    lista_completa = ['|'.join(each) for each in itertools.izip(autores_menciones,tweets)]
    del (autores_menciones)
    del (tweets)

   
    lista_autores = [getData (cad) for cad in lista_completa]


    #print lista_autores[0].getAutor()

    #for i in lista_autores:
    #    print i.getAll ()
    