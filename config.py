import pandas as pd




import csv
                    #Null reiksmiu trinimas
csv_file_path = 'scraped_data.csv'
output_file_path = 'scraped_data.csv'

with open(csv_file_path, 'r') as input_file:
    reader = csv.reader(input_file)
    header = next(reader)
    indices = {column: index for index, column in enumerate(header)}
    rows_without_null = [header]


    for row in reader:
        if not any(cell is None or cell == '' for cell in row):
            rows_without_null.append(row)
with open(output_file_path, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(rows_without_null)


                    #Stulpeliu formotavimas
current_delimiter = ','
new_delimiter = '|'

with open('output.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=current_delimiter)
    header = csvfile.readline().strip().split(current_delimiter)
    csvreader = csv.DictReader(csvfile, fieldnames=header, delimiter=current_delimiter)
    data = list(csvreader)


with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=header, delimiter=new_delimiter)
    csvwriter.writeheader()
    csvwriter.writerows(data)
print("openaq.csv")

                    #Stulpeliu pavadinimo keitimas
df = pd.read_csv('scraped_data.csv')
df.rename(columns={'0': 'ID'}, inplace=True)
df.rename(columns={'1': 'Country'}, inplace=True)
df.rename(columns={'2': 'Pollutant'}, inplace=True)
df.rename(columns={'3': 'Value'}, inplace=True)
df.rename(columns={'4': 'Unit'}, inplace=True)
df.rename(columns={'5': 'Last Update'}, inplace=True)
df.rename(columns={'6': 'Source Name'}, inplace=True)
df.to_csv("scraped_data.csv", index=False)
print(df)
