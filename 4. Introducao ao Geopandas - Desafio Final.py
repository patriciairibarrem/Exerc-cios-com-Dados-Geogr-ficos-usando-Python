#!/usr/bin/env python
# coding: utf-8

# ## ANÁLISES ESPACIAIS E CIÊNCIA DE DADOS GEOGRÁFICOS COM PYTHON
# 
# Exercícios referentes ao curso Spatial Analysis and Geospatial Data Science With Python da Udemy. 
# https://here.udemy.com/course/spatial-data-science-with-python/learn/lecture/20169360#overview

# # Desafio

# In[28]:


#Importar as bibliotecas: Geopandas, Pandas e Matplotlib.pyplot 
import geopandas as gpd
import pandas as pd
import matplotlib as plt


# # 1. Ler Dado Geográfico com Geopandas
# * Ler neighbourhoods "AssignmentData/Neighborhoods_Philadelphia/ com Geopandas. Use geopandas read_file() e dê um nome da sua escolha.
# * O dado que estamos lendo é um shapefile com o nome de "Neighborhoods_Philadelphia"

# In[13]:


#Mostrar as cinco primeiras linhas do dado

shp = r'C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\AssignmentData\Neighborhoods_Philadelphia\Neighborhoods_Philadelphia.shp'
bairros_test = gpd.read_file(shp)
bairros_test.head()


# In[14]:


#Visualize o dado com o método .plot() do geopandas
bairros_test.plot()


# In[35]:


#ler CSV com Pandas e converta para DataFrame
incidents_file = r'C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\AssignmentData\incidents.csv'
incidents = pd.read_csv(incidents_file)
incidents.head()


# In[36]:


#Mostre uma amostra de linhas desse dataFrame usando o método .sample() 
incidents.sample()


# In[37]:


#Converta o dataFrame para GeodataFrame usando o método gpd.GeoDataFrame()
incidents = gpd.GeoDataFrame(
    incidents, 
    geometry=gpd.points_from_xy(incidents.lng, incidents.lat)
)
incidents.head()


# In[40]:


#Visualize o GeoDataFrame com o método .plot() do geopandas
incidents.plot()


# In[41]:


#Tente usar indexing tendo a coluna de Latitude como condição ("lat" > 38) e os outliers serão removidos. 
incidents[incidents['lat'] > 38].head()


# In[42]:


#Visualizar o GeodataFrame limpo com o método .plot() do geopandas
incidents[incidents['lat'] > 38].plot()


# In[47]:


#Salve o arquivo como "incidents_clean_up.shp"
pasta = r'C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\AssignmentData'
incidents_shp = f'{pasta}\incidents.shp'
incidents.to_file(incidents_shp)

