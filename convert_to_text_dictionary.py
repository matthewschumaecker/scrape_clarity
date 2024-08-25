import json

def json_to_text(json_data):
    text_output = f"Table: {json_data['table_name']}\n"
    text_output += f"Description: {json_data['table_description']}\n"
    text_output += "Columns:\n"
    for column in json_data["columns"]:
        text_output += f"  - {column['column_name']} ({column['column_data_type']}): {column['column_description']}\n"
    return text_output


def create_text_dictionary(json_file):
    clarity_text_dictionary = ""
    json_data = open(json_file).read()
    for item in json.loads(json_data):
        clarity_text_dictionary += json_to_text(item)
        clarity_text_dictionary += '===============================================================================\n'
    return clarity_text_dictionary


print(create_text_dictionary("clarity_data_dictionary.json"))
with open("clarity_data_dictionary.txt", "w") as text_file:
    text_file.write(create_text_dictionary("clarity_data_dictionary.json"))
