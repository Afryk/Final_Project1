import folium
import requests
import pandas as pd
import requests
df = pd.read_csv('output.csv')
print(df)


Pollution = pd.read_csv('output.csv')
country_url = ("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/openaq/exports/geojson?lang=en&refine=country%3A%22LT%22&qv1=(LT)&timezone=Europe%2FHelsinki")

m = folium.Map(location=(55.1735998, 23.8948016), zoom_start=7, tiles="cartodb positron")
folium.GeoJson(country_url).add_to(m)
m.save('map.html')
Pollution['latitude'] = Pollution['Latitude'].astype(int)
Pollution['longitude'] = Pollution['Longitude'].astype(int)
for _, columns in df.iterrows():
    folium.Marker([columns['Latitude'], columns['Longitude']], popup=[
        columns['Location'],
        columns['Pollutant'],
        columns['Value']]
        ).add_to(m)
m.save('map.html')