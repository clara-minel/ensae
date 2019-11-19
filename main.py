            
"""Défintion des fonctions de notre module"""


    ##Fonction pour faire des pie-charts avec des variables numériques
   ## """importation des packages"

import numpy as np
import pandas
import chardet
import matplotlib.pyplot as plt
from plotly import tools
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
def piechart_num(var_cat_1,var_cat_2,var_num_1,var_num_2,year_1,year_2,name):
    """La fonction piechart_num permet, �  partir de 7 variables, d'afficher deux pie charts.
    L'argument var_cat_1 correspond �  une vecteur catégorielle d'une année n d'une base de donnée
    L'argument var_cat_2 correspond �  une vecteur catégorielle d'une année m d'une base de donnée
    L'argument var_num_1 correspond �  une vecteur quantitative de l'année n d'une base de donnée
    L'argument var_num_2 correspond �  une vecteur quantitative de l'année m d'une base de donnée
    L'argument year_1 correspond �  une année donnée
    L'argument year_2 correspond �  une autre année donnée, supposée supérieure �  n
    L'argument name correspond au nom que l'on veut donner �  la représentation"""
    c=var_cat_1.unique()
    d=var_cat_2.unique()
    list1=[]
    for v in c:
        print(v)
        x_v=0
        x_v+=sum(var_num_1[i] for i in range(len(var_num_1)) if var_cat_1[i]==v)
        print(x_v)
        list1.append(x_v)
    print(list1)
    list2=[]
    for v in d:
        print(v)
        x_v=0
        x_v+=sum(var_num_2[i] for i in range(len(var_num_2)) if var_cat_2[i]==v)
        print(x_v)
        list2.append(x_v)
    print(list2)
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=[year_1, year_2])
    fig.add_trace(go.Pie(labels=c,values=list1,scalegroup="one", name=year_1),1,1)
    fig.add_trace(go.Pie(labels=d,values=list2,scalegroup="one", name=year_2),1,2)
    fig.update_layout(title_text=name)
    fig.show()
    

    ##Fonction pour faire des pie-charts avec des variables catégorielles

def piechart_string(var_cat_1,var_cat_2,var_str_1,var_str_2,year_1,year_2,name):
    """La fonction piechart_string permet, �  partir de 7 variables, d'afficher deux pie charts.
    L'argument var_cat_1 correspond �  une vecteur catégorielle d'une année n d'une base de donnée
    L'argument var_cat_2 correspond �  une vecteur catégorielle d'une année m d'une base de donnée
    L'argument var_str_1 correspond �  une vecteur de string de l'année n d'une base de donnée
    L'argument var_str_2 correspond �  une vecteur de string de l'année m d'une base de donnée
    L'argument year_1 correspond �  une année donnée
    L'argument year_2 correspond �  une autre année donnée, supposée supérieure �  n
    L'argument name correspond au nom que l'on veut donner �  la représentation"""
    c=var_cat_1.unique()
    d=var_cat_2.unique()
    list1=[]
    for v in c:
        print(v)
        x_v=0
        for i in range(len(var_cat_1)):
            if var_cat_1[i]==v:
                x_v+=1 
        print(x_v)
        list1.append(x_v)
    print(list1)
    list2=[]
    for v in d:
        print(v)
        x_v=0
        for i in range(len(var_cat_2)):
            if var_cat_2[i]==v:
                x_v+=1 
        print(x_v)
        list2.append(x_v)
    print(list2)
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=[n, m])
    fig.add_trace(go.Pie(labels=c,values=list1,scalegroup="one", name=year_1),1,1)
    fig.add_trace(go.Pie(labels=d,values=list2,scalegroup="one", name=year_2),1,2)
    fig.update_layout(title_text=name)
    fig.show()
   
    
    ## Fonction pour les cartes

def plot_geo_time_value(data,variable_of_interest,coordinates,nb_of_periods,title='Titre',plots_per_row=2,plots_per_column=2, scale = 1/40):
    
    """ data, variable_of_interest, coordinates déj�  présentés
    nb_of_periods : le nombre de cartes que l'on veut représenter
    title : le titre que l'on veut donner aux cartes
    plots_per_row : nb de cartes par ligne
    plots_per_columns : nb de cartes par colonne"""
    
    
    fig = plt.figure(figsize=(15,10)) 

    color_ticker = ['green','orange','red','mediumpurple','blue','black','olivedrab','firebrick','aqua','lightcoral','gold','teal','mediumorchid','coral','yellow','lightblue','fuschia']
    

    for i in range(1,nb_of_periods+1):
    
        ax = fig.add_subplot(plots_per_column,plots_per_row,i,projection=ccrs.PlateCarree())
        ax.set_extent(lim_metropole)
        ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
        ax.add_feature(cfeature.RIVERS.with_scale('50m'))
        ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')
        ax.scatter(data[i-1][coordinates[i-1][0]], data[i-1][coordinates[i-1][1]],
           s=data[i-1][variable_of_interest[i-1]] ** scale, alpha=0.5, color = color_ticker[i-1])
        ax.set_title(titles[i-1])

    fig.suptitle(title, fontsize=16)
    fig.show()


    ## La fonction barplot permet de réaliser un histogramme avec des variables catégorielles 

def barplot_variations(a,b,h1,h2,absc,ordo,z,title,df19,df18):
    
    column1= h1
    column4= h2
    column2= a
    column3= b

    
    df19sum = df19.groupby(column1)[column3].sum()

    df18sum = df18.groupby(column4)[column2].sum() 
         
    df18sum=pandas.DataFrame(df18sum)
    df19sum=pandas.DataFrame(df19sum)
    df18sum.rename(columns={a: 'V1'}, inplace=True)
    df19sum.rename(columns={b: 'V2'}, inplace=True)
    df2=pandas.merge(df18sum,df19sum, on=h1 )
    df2['Variation']=(df2['V2']-df2['V1'])*100/df2['V1']
    df2['categorie'] =  df2.index


    plt.bar(x=np.arange(1,z),height=df2['Variation'])
    plt.title(title)
    plt.xlabel(absc)
    plt.ylabel(ordo)
    plt.xticks(np.arange(1,z), df2['categorie'], rotation=90)

    plt.show()
