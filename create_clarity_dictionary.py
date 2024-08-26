from bs4 import BeautifulSoup
import json, requests

def fetch_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def get_table_links():
    html_content = fetch_html_content("https://open.epic.com/EHITables/GetTable/_index.htm")
    index_soup = BeautifulSoup(html_content, 'html.parser')

    tables = index_soup.find_all('a', href=True)
    table_links = []
    for table in tables:
        if table['href'].startswith('./'):
            table_links.append(table['href'][2:])
    return table_links # returns a list of table links SUFFIXES

def get_table_data(table_name):
    link = f'https://open.epic.com/EHITables/GetTable/{table_name}'
    print(f"Extracting data from {link}...")
    html_content = fetch_html_content(link)
    soup = BeautifulSoup(html_content, 'html.parser')

    table_name = soup.find('table', class_='Header2').text
    info_results = soup.find_all('td', class_='T1Head')
    info_description = soup.find_all('td', style="white-space: normal;")
    table_description = info_description[0].text

    columns = []
    for i in range(1, len(info_results),3):
        column = {
            "column_name": info_results[i + 1].text,
            "column_data_type": info_results[i + 2].text,
            "column_description": info_description[int((i+2)/3)].text
        }
        columns.append(column)
    table_dict=  {"table_name":table_name,"table_description":table_description,"columns":columns}
    return table_dict

def main():
    data_dictionary=[]
    for link in get_table_links():
        data_dictionary.append(get_table_data(link))
        print(f"Writing {link} to data_dictionary...")

    with open("clarity_data_dictionary.json", "w") as outfile:
        print(f"converting dictionary to json file: 'clarity_data_dictionary.json'")
        json.dump(data_dictionary, outfile, indent=4)
