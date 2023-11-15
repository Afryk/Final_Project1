from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get(
        'https://public.opendatasoft.com/explore/dataset/openaq/table/?disjunctive.city&disjunctive.location&disjunctive.measurements_parameter&sort=measurements_parameter&q=LT&refine.country=LT&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibWVhc3VyZW1lbnRzX3ZhbHVlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoicmFuZ2UtY3VzdG9tIn1dLCJ4QXhpcyI6Im1lYXN1cmVtZW50c19sYXN0dXBkYXRlZCIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJtZWFzdXJlbWVudHNfcGFyYW1ldGVyIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJvcGVuYXEiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLmNpdHkiOnRydWUsImRpc2p1bmN0aXZlLmxvY2F0aW9uIjp0cnVlLCJkaXNqdW5jdGl2ZS5tZWFzdXJlbWVudHNfcGFyYW1ldGVyIjp0cnVlLCJzb3J0IjoibWVhc3VyZW1lbnRzX2xhc3R1cGRhdGVkIn19fV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=7,55.38223,24.47205&basemap=jawg.light')
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'odswidget-table__records')))

    rows = table.find_elements(By.TAG_NAME, 'tr')

    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        col_data = [col.text for col in cols]
        data.append(col_data)

    if data:
        headers = data.pop(0) if data[0] else None
        df = pd.DataFrame(data, columns=headers)

        csv_file_path = 'scraped_data.csv'
        df.to_csv(csv_file_path, index=False)
        print(f'Data written to {csv_file_path}')
    else:
        print("No data scraped.")
finally:
    driver.quit()