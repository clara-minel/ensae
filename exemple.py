# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:03:02 2019

@author: clara
"""


            
                          ## """Exemple d'utilisation du module main.py avec les donnees de l'ADEME"


   ## """importation des packages"

import numpy as np
import pandas
import chardet
import matplotlib.pyplot as plt
from plotly import tools
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
#import ensae_teaching_cs.data

    ##"""importation du module"
import Module.main as main
from Module.main import *
     ##"""importation des donnees"

df19 = pandas.read_excel("DEAL Flow automatisation.xlsx", decimal=',')
df18 = pandas.read_csv("Jeu de données deal flow 2018.csv", encoding='Windows-1252', sep=';', decimal=',')



try:
    main.piechart_num(df18.SOUS_DOMAINE, df19.SOUS_DOMAINE,df18.iMontantTotal , df19['iMontant total'], '2018', '2019', 'Investissements par domaine')
    main.piechart_string(df18.SOUS_DOMAINE, df19.SOUS_DOMAINE, df18.DOSSIER_CODE, df19.DOSSIER_CODE, '2018', '2019', "Nombre d'investissements par domaine")
except:
    main.piechart_num(df18['SOUS_DOMAINE'], df19['SOUS_DOMAINE'],df18['iMontantTotal'] , df19['iMontant total'], '2018', '2019', 'Investissements par domaine')
    main.piechart_string(df18['SOUS_DOMAINE'], df19['SOUS_DOMAINE'], df18['DOSSIER_CODE'], df19['DOSSIER_CODE'], '2018', '2019', "Nombre d'investissements par domaine")

main.barplot_variations(df18['iMontantTotal'], df19['iMontant total'],df18.SOUS_DOMAINE,"Evolution des montants investis selon les différents domaines par l'ADEME entre 2018 et 2019 en pourcentage", 'Sous domaines', 'Montant investi',5)


df18 = df18.dropna()
df19 = df19.dropna()

    ##"""Définition des limites de la France métropole"
lim_metropole = [-5, 10, 41, 52]

    ##"""On conserve uniquement les projets de France métropolitaine"
df18_metro = df18[((df18.COMMUNE_X >= lim_metropole[0]) & (df18.COMMUNE_X <= lim_metropole[1]) &
                (df18.COMMUNE_Y >= lim_metropole[2]) & (df18.COMMUNE_Y <= lim_metropole[3]))]
    
df19_metro = df19[((df19.COMMUNE_X >= lim_metropole[0]) & (df19.COMMUNE_X <= lim_metropole[1]) &
                (df19.COMMUNE_Y >= lim_metropole[2]) & (df19.COMMUNE_Y <= lim_metropole[3]))]



main.plot_geo_time_value(data,variable_of_interest,coordinates,nb_of_periods,titles)