 # imports
import panel as pn
pn.extension('plotly')
import plotly.express as px
import pandas as pd
import hvplot.pandas
import matplotlib.pyplot as plt
import os
from pathlib import Path
from dotenv import load_dotenv
# Import Data
production_path = Path("../data/Total_Energy_Production.csv")
consumption_path = Path("../data/Total_Energy_Use.csv")
Total_Energy_Nominal_Path = Path("../data/Total_Energy_Nominal_Prices.csv")
Renewable_Consumption_path = Path("../data/Renewable_Energy_Consumption.csv")
Renewable_Path = Path("../data/Renewable_Production.csv")

production_data = pd.read_csv(production_path)
consumption_data = pd.read_csv(consumption_path)
renewable_consumption = pd.read_csv(Renewable_Consumption_path, index_col="Year")
renewable_production_data = pd.read_csv(Renewable_Path, index_col="Year")
Total_Energy_Nominal_data = pd.read_csv(Total_Energy_Nominal_Path)
Prod_Price_combined_df = pd.concat([production_data, Total_Energy_Nominal_data], axis="columns", join="inner")
Consu_Price_combined_df = pd.concat([consumption_data, Total_Energy_Nominal_data], axis="columns", join="inner")
Consu_Prod_combined_df = pd.concat([consumption_data, production_data], axis="columns", join="inner")
# Define Panel Visualization Functions

def Production_plot():
    """Production Plot"""
    
    Production = production_data.loc[:, [ 'Year','Crude Oil and Lease Condensate quads', 'Natural Gas Plant Liquids quads', 'Coal quads', 'Nuclear quads', 'Hydropower quads', 'Other Renewable Energy quads']]

    return Production.hvplot.line(x='Year', y=['Crude Oil and Lease Condensate quads', 'Natural Gas Plant Liquids quads', 'Coal quads', 'Nuclear quads','Hydropower quads','Other Renewable Energy quads']).opts(title="Production", width=600)

def Production_bargraph():
    """Production Bargraph"""

    Production = production_data.loc[:, [ 'Year','Crude Oil and Lease Condensate quads', 'Natural Gas Plant Liquids quads', 'Coal quads', 'Nuclear quads', 'Hydropower quads', 'Other Renewable Energy quads']]

    return Production.hvplot.bar(x='Year', y=['Crude Oil and Lease Condensate quads', 'Natural Gas Plant Liquids quads', 'Coal quads', 'Nuclear quads','Hydropower quads','Other Renewable Energy quads'], height=600, width=1200, rot=90)

def Consumption_linegraph():
    """Consumption Line Graph"""

    consumption = consumption_data.loc[:,['Year','Liquid Fuels quads', 'Natural Gas quads','Coal quads', 'Nuclear quads', 'Hydropower quads', 'Other Renewable Energy quads']]

    return consumption.hvplot.line(x='Year', y=[ 'Liquid Fuels quads', 'Natural Gas quads','Coal quads', 'Nuclear quads','Hydropower quads','Other Renewable Energy quads']).opts(title="Consumption Line", width=600)

def Consumption_Bargraph():
    """Consumption Bar Graph"""

    consumption = consumption_data.loc[:,['Year','Liquid Fuels quads', 'Natural Gas quads','Coal quads', 'Nuclear quads', 'Hydropower quads', 'Other Renewable Energy quads']]

    return consumption.hvplot.bar(x='Year', y=['Liquid Fuels quads', 'Natural Gas quads','Coal quads', 'Nuclear quads','Hydropower quads','Other Renewable Energy quads'], height=600, width=1200, rot=90)

def Nonrenewable_Production():
    """Non-renewable Production"""

    Production = production_data.loc[:, [ 'Year','Crude Oil and Lease Condensate quads', 'Natural Gas Plant Liquids quads', 'Coal quads', 'Nuclear quads']]

    return Production.hvplot.line(x='Year', y=['Crude Oil and Lease Condensate quads', 'Natural Gas Plant Liquids quads', 'Coal quads', 'Nuclear quads'], title='Nonrenewable Energy Production')

def Renewable_Production():
    """Renewable Production"""

    Production = production_data.loc[:, ['Year','Hydropower quads', 'Biomass quads',	'Other Renewable Energy quads']]

    return Production.hvplot.line(x='Year', y=['Hydropower quads','Biomass quads',	'Other Renewable Energy quads'], title='Renewable Energy Production')

def Renewable_Energy_Barchart():
    """Renewable Energy Barchart"""

    Production = production_data.loc[:, ['Year','Hydropower quads', 'Biomass quads',	'Other Renewable Energy quads']]

    return Production.hvplot.bar(
    title= "Renewable Energy Production", 
    x='Year', 
    y=['Hydropower quads', 'Biomass quads', 'Other Renewable Energy quads'], height=500, width=800, rot=90

)

def Renewable_Consumption_Line():
    """Renewable Consumption Line"""

    consumption = consumption_data.loc[:,['Year','Hydropower quads', 'Biomass quads', 'Other Renewable Energy quads' ]]

    return consumption.hvplot.line(
    title= "Renewable Energy Consumption", 
    x='Year', 
    y=[ 'Hydropower quads','Biomass quads', 'Other Renewable Energy quads']

)

def Nonrenewable_Consumption_Line():
    """Non-renewable Consumption Line"""

    consumption = consumption_data.loc[:,['Year','Liquid Fuels quads', 'Natural Gas quads','Coal quads', 'Nuclear quads']]

    return consumption.hvplot.line(
    title= "Nonrenewable Energy Consumption", 
    x='Year', 
    y=[ 'Liquid Fuels quads', 'Natural Gas quads','Coal quads', 'Nuclear quads']

)

    return map
consumption_data = consumption_data.iloc[20:-1]
production_data = production_data.iloc[15:-1]

welcome_tab = pn.Column('#Energy', Production_plot)
row = pn.Row(Production_bargraph, Consumption_linegraph, Consumption_Bargraph)
renewable_graphs = pn.Column('Renewable Energy', row)
column = pn.Column('Non-Renewable Energy', Nonrenewable_Production, Renewable_Production, Renewable_Energy_Barchart, Renewable_Consumption_Line, Nonrenewable_Consumption_Line)
panel = pn.Tabs(
    ("Welcome", welcome_tab),
    ("Renewable Energy", renewable_graphs),
    ("Non-Renewable Energy", column))
panel.servable()
