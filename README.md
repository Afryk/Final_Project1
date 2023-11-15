


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
2. Naudojant geoJson URL https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/openaq/exports/geojson?lang=en&refine=country%3A%22LT%22&qv1=(LT)&timezone=Europe%2FHelsinki žemėlapyje nurodome Lietuvos lokaciją.
3. Naudojant output.csv nurodome tikslias matavimo stočių kordinates ir kenksmingų medžiagų reikšmes.

### Analize.py:

1. Suradome skirtingų kenksmingų dalelių dienos vidurkį Lietuvoje.
2. Procentaliai identifikavom labiausiai paplitusią kenksmingą medžiaga
3. Identifikavom labiausiai užterštus lietuvos miestus.



### Išvada:

Labiausiai dominuojanti kenksminga medžiaga Lietuvoje yra anglies dioksidas.
Labiausiai užteršti Lietuvos miestai yra Panevežys, Klaipėda ir Šiauliai.


