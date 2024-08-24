from bs4 import BeautifulSoup
import json



with open('sample.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'html.parser')


# grabs index, column name and data type in that order
table_name_results = soup.find(name= 'table', class_="Header2")
info_results = soup.find_all('td', class_="T1Head")
desc_results = soup.find_all('td', style="white-space: normal;")

table_name = table_name_results.text
table_desc = desc_results[0].text
columns = []

for i in range (1, len(info_results),3):

    column = {
    "column number": info_results[i].text,
    "column name": info_results[i+1].text,
    "column data type" : info_results[i+2].text,

             }

    columns.append(column)
for i in range (0, len(desc_results)-1):
    columns[i]['column description'] = desc_results[i+1].text

table = {
    'table_name': table_name,
    'table_description:': table_desc,
    'columns:': columns
}

output = json.dumps(table, indent=4)

print(output)