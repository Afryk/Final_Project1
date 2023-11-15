


      # Oro kokybės monitoringo ir analizės sistema  

## Aprašymas

Darbą atliko Erikas Kupčiūnas ir Andzhej Trusevich

Tai yra baigiamasis Vilnius Coding school projektas

Projekto tema: Oro kokybės monitoringo ir analizės sistema

Pagrindinis projekto tikslas: Remiantis patikimais oro monitoringo šaltiniais, sukurti įrankius, kurie padėtų išanalizuoti Lietuvos bendrą užterštumo vidurkį.

Šiame projekte mes dirbome su Python programavimo kalba, naudojome CSV formato failus.

## Pritaikytos Žinios:

Mūsų naudotos biliotekos: Selenium, Pandas, Matplotlib, Folium.

### Scraping.py:

1. Suradome patikimą oro monitoringo tinklalapį: https://public.opendatasoft.com/explore/dataset/openaq/table/?disjunctive.city&disjunctive.location&disjunctive.measurements_parameter&sort=measurements_lastupdated
2. Ištraukėme reikiamą informaciją naudojant Selenium Webdriver biblioteką. Informaciją išsaugojome CSV faile pavadinimu "scraped_data.csv"
3. Atsisiuntėm kitą CSV failą su mums trūkstama infromacija. Failo pavadinimas: "openaq.csv"

### Config.py:

1. Isvalėm lentelę scraped_data.csv faile nuo NULL reikšmių.
2. Surašėm naujus stulpeliu pavadinimus faile scraped_data.csv
3. Perdarėm openaq.csv esamą netvarkingą ir prastai suformatuotą lentlę ir pervadinom į output.csv


### Map.py:

1. Naudojant Folium ir Pandas bibliotekas sukūrėme interaktyvų Lietuvos žemėlapį, kuriame yra rodomi oro kokybes matuokliai.


![Map](C:\Users\erika\PycharmProjects\DemoProject\Screenshots)
<img src="C:\Users\erika\PycharmProjects\DemoProject\Screenshots" alt="Map" width="600"/>